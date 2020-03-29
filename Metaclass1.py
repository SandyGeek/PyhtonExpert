class ParentClass:
    def parent(self):
        print("Hey Mota!!")


MetaClass = type('MClass', (ParentClass,), {'u': 5})
mc = MetaClass()
print(mc.u)
print("Type of ParentClass class is:", type(ParentClass))
print(mc.parent())
