"""Import another py file"""
#import file
import new_import
new_import.test()

#reload the import file
reload(new_import)
print "After reload"

#imported file function
new_import.test()
