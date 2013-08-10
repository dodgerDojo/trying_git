class f:
    def __init__(self):
        self.x = 54;
        
    def __enter__(self):
        print "Hey"
        
    def __exit__(self, type, value, traceback):
        print "bye"

print "My name is Dan"
my_list = [1,2,3]
for x in range(4):
    if x in my_list:
        print "He is!"
        
def y():
    print "Nice."
    
a = f()
with a as f:
    print "I'm Here."