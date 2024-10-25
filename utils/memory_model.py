import tracemalloc
import gc
import inspect
import copy
import sys
from termcolor import colored

class MemoryModelVisualizer:
    def __init__(self):
        self.previous_objects = {}
        tracemalloc.start()

    def trace_calls(self, frame, event, arg):
        """Trace each line executed inside functions."""
        if event != 'line':
            return
        co = frame.f_code
        lineno = frame.f_lineno
        filename = co.co_filename
        line = open(filename).readlines()[lineno - 1].strip()
        print(f"\nExecuting Line {lineno}: {line}")
        return self.trace_calls

    def capture_memory_state(self, step_label):
        """Capture and compare memory state, logging changes."""
        sys.settrace(self.trace_calls)  # Start tracing function calls
        current_objects = self._get_objects()
        added, removed, modified = self._compare_states(self.previous_objects, current_objects)

        # Log changes or display if no change occurred
        if added or removed or modified:
            print(f"\n[Change Log Before Step: {step_label}]")
            self._log_changes(added, removed, modified)
        else:
            print(f"\n[No Changes Detected at Step: {step_label}]")
            self._display_unchanged_objects(current_objects)

        print(f"\n[Memory Model: {step_label}]")
        self._display_memory_model(current_objects)

        self.previous_objects = copy.deepcopy(current_objects)  # Update for next step
        sys.settrace(None)  # Stop tracing

    def _get_objects(self):
        """Retrieve all objects in memory with details."""
        gc.collect()
        objects = {}
        frame = inspect.currentframe().f_back

        for var_name, var_value in frame.f_locals.items():
            obj_id = id(var_value)
            obj_type = type(var_value).__name__
            obj_value = self._get_object_value(var_value)
            objects[obj_id] = {"name": var_name, "type": obj_type, "value": obj_value, "ref": var_value}
        return objects

    def _get_object_value(self, obj):
        """Get a string representation of the object's value."""
        if isinstance(obj, (list, tuple, set)):
            return [f"({id(item)}, {repr(item)[:20]})" for item in obj]
        elif isinstance(obj, dict):
            return {id(k): f"({repr(k)[:10]}: {repr(v)[:20]})" for k, v in obj.items()}
        else:
            return repr(obj)[:50]

    def _compare_states(self, old, new):
        """Detect added, removed, and modified objects."""
        added = {k: new[k] for k in new if k not in old}
        removed = {k: old[k] for k in old if k not in new}
        modified = {
            k: (old[k], new[k])
            for k in new
            if k in old and self._is_modified(old[k]["ref"], new[k]["ref"])
        }
        return added, removed, modified

    def _is_modified(self, old_obj, new_obj):
        """Detect if a mutable object was modified in-place."""
        if isinstance(old_obj, (list, dict, set)):
            return old_obj != new_obj
        return id(old_obj) != id(new_obj)

    def _log_changes(self, added, removed, modified):
        """Log added, removed, and modified objects."""
        frame = inspect.currentframe().f_back
        line_number = frame.f_lineno
        source_line = inspect.getframeinfo(frame).code_context[0].strip()
        highlighted_line = self._highlight_expression(source_line, added, removed, modified)

        print(f"\nLine {line_number}: {highlighted_line}")

        if added:
            print("\n[Added Objects]")
            for obj_id, obj in added.items():
                print(f"{obj['name']} | {obj_id} | {obj['type']} | {obj['value']}")

        if removed:
            print("\n[Removed Objects]")
            for obj_id, obj in removed.items():
                print(f"{obj['name']} | {obj_id} | {obj['type']} | {obj['value']}")

        if modified:
            print("\n[Modified Objects]")
            for obj_id, (old_obj, new_obj) in modified.items():
                print(
                    f"{new_obj['name']} | {obj_id} | {new_obj['type']} | "
                    f"{colored('~~' + str(old_obj['value']) + '~~', 'red')} -> {new_obj['value']}"
                )

    def _highlight_expression(self, line, added, removed, modified):
        """Highlight the part of the expression that caused the change."""
        for obj in added.values():
            line = line.replace(obj['name'], colored(f"{obj['name']}", "green"))
        for obj in removed.values():
            line = line.replace(obj['name'], colored(f"{obj['name']}", "red"))
        for old_obj, new_obj in modified.items():
            line = line.replace(new_obj[1]['name'], colored(f"{new_obj[1]['name']}", "yellow"))
        return line

    def _display_unchanged_objects(self, objects):
        """Display unchanged objects for reference."""
        print("\n[Unchanged Objects]")
        for obj_id, obj in objects.items():
            print(f"{obj['name']} | {obj_id} | {obj['type']} | {obj['value']}")

    def _display_memory_model(self, objects):
        """Display the complete memory model."""
        print("\nObject Name | ID | Type | Value")
        print("-" * 50)
        for obj_id, obj in objects.items():
            print(f"{obj['name']} | {obj_id} | {obj['type']} | {obj['value']}")

# Example usage with function calls
def modify_list(lst):
    lst.append("new item")  # Modify in-place

def reassign_variable(var):
    var = "new value"  # Creates a new string object

if __name__ == "__main__":
    visualizer = MemoryModelVisualizer()

    # Initial list of variables
    print("\n[Initial List of Variables]")
    visualizer.capture_memory_state("Initial")

    # Modify list (in-place)
    modify_list([1, 2, 3])
    visualizer.capture_memory_state("After modifying list")

    # Reassign string (new object)
    reassign_variable("hello")
    visualizer.capture_memory_state("After reassigning string")

    # Final memory model
    print("\n[Final Memory Model]")
    visualizer.capture_memory_state("Final")
