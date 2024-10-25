from rich.console import Console
from rich.table import Table
import tracemalloc
import gc
import inspect
import copy
import sys

class MemoryModelVisualizer:
    def __init__(self):
        self.previous_objects = {}
        self.console = Console()
        tracemalloc.start()

    def trace_calls(self, frame, event, arg):
        """Trace each line executed inside functions."""
        if event != 'line':
            return
        co = frame.f_code
        lineno = frame.f_lineno
        filename = co.co_filename
        line = open(filename).readlines()[lineno - 1].strip()
        self.console.print(f"\n[cyan]Executing Line {lineno}:[/cyan] {line}")
        return self.trace_calls

    def capture_memory_state(self, step_label):
        """Capture and compare memory state, logging changes."""
        sys.settrace(self.trace_calls)  # Start tracing function calls
        current_objects = self._get_objects()
        added, removed, modified, inactive = self._compare_states(self.previous_objects, current_objects)

        if added or removed or modified or inactive:
            self.console.print(f"\n[bold magenta]Change Log Before Step: {step_label}[/bold magenta]")
            self._log_changes(added, removed, modified, inactive)
        else:
            self.console.print(f"\n[bold green]No Changes Detected at Step: {step_label}[/bold green]")

        self.console.print(f"\n[bold yellow]Memory Model: {step_label}[/bold yellow]")
        self._display_memory_model(current_objects)

        self.previous_objects = copy.deepcopy(current_objects)  # Update for next step
        sys.settrace(None)  # Stop tracing

    def _get_objects(self):
        """Retrieve all objects in memory with their scope."""
        gc.collect()
        objects = {}
        frame = inspect.currentframe().f_back

        # Check local variables in the current frame
        for var_name, var_value in frame.f_locals.items():
            scope = "local"
            if var_name in frame.f_globals:
                scope = "global"
            obj_id = id(var_value)
            obj_type = type(var_value).__name__
            obj_value = self._get_object_value(var_value)
            objects[obj_id] = {
                "name": var_name,
                "type": obj_type,
                "value": obj_value,
                "scope": scope,
                "ref": var_value,
            }
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
        """Detect added, removed, modified, and inactive objects."""
        added = {k: new[k] for k in new if k not in old}
        removed = {k: old[k] for k in old if k not in new}
        modified = {
            k: (old[k], new[k])
            for k in new
            if k in old and self._is_modified(old[k]["ref"], new[k]["ref"])
        }
        inactive = {k: old[k] for k in old if k not in new and old[k]["scope"] == "local"}
        return added, removed, modified, inactive

    def _is_modified(self, old_obj, new_obj):
        """Detect if a mutable object was modified in-place."""
        if isinstance(old_obj, (list, dict, set)):
            return old_obj != new_obj
        return id(old_obj) != id(new_obj)

    def _log_changes(self, added, removed, modified, inactive):
        """Log changes in variables."""
        if added:
            self.console.print("\n[bold green]Added Objects:[/bold green]")
            self._display_objects_table(added)

        if removed:
            self.console.print("\n[bold red]Removed Objects:[/bold red]")
            self._display_objects_table(removed)

        if modified:
            self.console.print("\n[bold yellow]Modified Objects (Old vs New):[/bold yellow]")
            self._display_modified_objects(modified)

        if inactive:
            self.console.print("\n[bold blue]Inactive Objects (Out of Scope):[/bold blue]")
            self._display_objects_table(inactive)

    def _display_modified_objects(self, modified):
        """Display modified objects with old and new values side by side."""
        table = Table(show_header=True, header_style="bold yellow")
        table.add_column("Object Name", style="cyan")
        table.add_column("ID", style="yellow")
        table.add_column("Type", style="green")
        table.add_column("[Old]", style="red")
        table.add_column("[New]", style="white")

        for obj_id, (old_obj, new_obj) in modified.items():
            table.add_row(
                new_obj['name'], str(obj_id), new_obj['type'],
                str(old_obj['value']), str(new_obj['value'])
            )

        self.console.print(table)

    def _display_memory_model(self, objects):
        """Display the complete memory model."""
        self.console.print("\n[bold]Memory Model:[/bold]")
        self._display_objects_table(objects)

    def _display_objects_table(self, objects):
        """Display objects in a table format."""
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Object Name", style="cyan")
        table.add_column("ID", style="yellow")
        table.add_column("Type", style="green")
        table.add_column("Scope", style="blue")
        table.add_column("Value", style="white")

        for obj_id, obj in objects.items():
            table.add_row(obj['name'], str(obj_id), obj['type'], obj['scope'], str(obj['value']))

        self.console.print(table)

# Example usage
def modify_global():
    global my_list
    my_list.append("new item")  # Modify global list

def local_scope_function():
    local_var = "I'm local"
    print(local_var)  # Local variable will become inactive

if __name__ == "__main__":
    visualizer = MemoryModelVisualizer()

    # Initial list of variables
    my_list = [1, 2, 3]
    my_str = "hello"
    visualizer.capture_memory_state("Initial")

    # Modify global list
    modify_global()
    visualizer.capture_memory_state("After modifying global list")

    # Call function with local scope
    local_scope_function()
    visualizer.capture_memory_state("After local scope function")

    # Final memory model
    visualizer.capture_memory_state("Final")
