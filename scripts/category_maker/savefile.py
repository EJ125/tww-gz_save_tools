class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class PracticeSaveInfo:
    def __init__(self, requirements, p0, angle, position, cam_pos, cam_target, counter, filename, p1):
        self.requirements = requirements
        self.p0 = p0
        self.angle = angle
        self.position = position
        self.cam_pos = cam_pos
        self.cam_target = cam_target
        self.counter = counter
        self.filename = filename
        self.p1 = p1