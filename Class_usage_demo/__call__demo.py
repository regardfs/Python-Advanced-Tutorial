class g_dpm(object):
    def __init__(self, g):
        self.g = g
    def __call__(self, t):
        return (self.g*t**2)/2

# e_dpm = g_dpm(9.8)
# when there is a __call__ in instance initial, it could execute.