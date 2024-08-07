from vector import Vector

class Object:
    ...

def create_object(name: str) -> Object | None: ...
def delete_object(o: Object) -> None: ...

def get_guid(o: Object) -> int: ...
def from_guid(guid: int) -> Object | None: ...

def enable(o: Object, state: bool, recursive: bool = False) -> None: ...
def is_enabled(o: Object) -> bool: ...

def pause(o: Object, state: bool, recursive: bool = False) -> None: ...
def is_paused(o: Object) -> bool: ...

def set_owner(o: Object, owner: Object | None) -> None: ...
def get_owner(o: Object) -> Object | None: ...

def find_owned_child(o: Object, path: str) -> Object | None: ...

def set_flip(o: Object, flip_x: bool, flip_y: bool) -> None: ...
def get_flip(o: Object) -> tuple[bool, bool]: ...

def set_position(o: Object, position: Vector, world: bool = False) -> None: ...
def get_position(o: Object, world: bool = False) -> Vector: ...

def set_parent(o: Object, parent: Object | None) -> None: ...
def get_parent(o: Object) -> Object | None: ...

def find_child(o: Object, path: str) -> Object | None: ...

def attach(o: Object, parent: Object) -> None: ...
def detach(o: Object) -> None: ...

def log_parents(o: Object) -> None: ...

def set_anim_frequency(o: Object, frequency: float, recursive: bool = False) -> None: ...
def get_anim_frequency(o: Object) -> float: ...
def set_anim_time(o: Object, time: float, recursive: bool = False) -> None: ...
def get_anim_time(o: Object) -> float: ...
def set_current_anim(o: Object, name: str, recursive: bool = False) -> None: ...
def get_current_anim(o: Object) -> str: ...
def set_target_anim(o: Object, name: str, recursive: bool = False) -> None: ...
def get_target_anim(o: Object) -> str: ...

def set_speed(o: Object, speed: Vector, relative = False) -> None: ...
def get_speed(o: Object, relative: bool = False) -> Vector: ...

def set_angular_velocity(o: Object, velocity: float) -> None: ...
def get_angular_velocity(o: Object) -> float: ...

def set_custom_gravity(o: Object, dir: Vector) -> None: ...
def get_custom_gravity(o: Object) -> Vector: ...

def get_mass(o: Object) -> float: ...
def get_mass_center(o: Object) -> Vector: ...

def apply_torque(o: Object, torque: float) -> None: ...
def apply_force(o: Object, force: Vector, point: Vector) -> None: ...
def apply_impulse(o: Object, impulse: Vector, point: Vector) -> None: ...

def raycast(begin: Vector, end: Vector, self_flags: int, check_mask: int, early_exit: bool = False) -> tuple[Object, Vector, Vector] | None: ...

def set_text_string(o: Object, s: str) -> None: ...
def get_text_string(o: Object) -> str: ...

def add_fx(o: Object, name: str, recursive: bool = False, unique: bool = True, propagation_delay: float = 0) -> None: ...
def remove_fx(o: Object, name: str, recursive: bool = False) -> None: ...
def remove_all_fxs(o: Object, recursive: bool = False) -> None: ...

def add_sound(o: Object, name: str) -> None: ...
def remove_sound(o: Object, name: str) -> None: ...
def remove_all_sounds(o: Object) -> None: ...
def set_volume(o: Object, volume: float) -> None: ...
def set_pitch(o: Object, pitch: float) -> None: ...
def set_panning(o: Object, panning: float, mix: bool) -> None: ...
def play(o: Object) -> None: ...
def stop(o: Object) -> None: ...
def add_filter(o: Object, name: str) -> None: ...
def remove_last_filter(o: Object) -> None: ...
def remove_all_filters(o: Object) -> None: ...

def add_shader(o: Object, name: str, recursive: bool = False) -> None: ...
def remove_shader(o: Object, name: str, recursive: bool = False) -> None: ...
def enable_shader(o: Object, enabled: bool = True) -> None: ...
def is_shader_enabled(o: Object) -> bool: ...

def add_time_line_track(o: Object, name: str, recusive: bool = False) -> None: ...
def remove_time_line_track(o: Object, name: str, recursive: bool = False) -> None: ...
def enable_time_line(o: Object, enabled: bool = True) -> None: ...
def is_time_line_enabled(o: Object) -> bool: ...

def add_trigger(o: Object, name: str, recursive: bool = False) -> None: ...
def remove_trigger(o: Object, name: str, recursive: bool = False) -> None: ...
def fire_trigger(o: Object, name: str, recursive: bool = False) -> None: ...

def get_name(o: Object) -> str: ...

def set_rgb(o: Object, rgb: Vector, recursive: bool = False) -> None: ...
def get_rgb(o: Object) -> Vector: ...

def set_alpha(o: Object, alpha: float, recursive: bool = False) -> None: ...
def get_alpha(o: Object) -> float: ...

def set_life_time(o: Object, life_time: float | str | None) -> None: ...
def get_life_time(o: Object) -> float | None: ...

def get_active_time(o: Object) -> float: ...
def reset_active_time(o: Object, recursive: bool = False) -> None: ...
