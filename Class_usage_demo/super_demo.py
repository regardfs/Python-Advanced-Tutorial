# before we use super in child class ,we should check out the __mro__ attribute first
# if we do not find __mro__, we should pay more attention, and try to avoid super()
# so, we should make super usage synchronously!!!
