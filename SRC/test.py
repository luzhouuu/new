import SRC.main as Main
import SRC.RequestGoTag as RequestGoTag

prompt_temp = 'aaa'
cap = Main.predict(prompt_temp, 'Capability')

print(cap)
print(Main.get_tagId(cap, 'Capability'))

taglable = Main.predict(prompt_temp, 'Sub-Capability', Main.get_tagId(cap, 'Capability'))

print(taglable)