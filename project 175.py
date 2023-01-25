import matplotlib .pyplot as plt
import psutil as p
app_name_dict = {}
count = 0
for process in p.process_iter():
    count = count + 1
    if count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print('name : ', name,'-- cpu_usage : ', cpu_usage)
        app_name_dict.update({name:cpu_usage})
        
keymax=max(app_name_dict,key=app_name_dict.get)
keymin=min(app_name_dict,key=app_name_dict.get)
name_list=[keymax,keymin]
print(name_list)

app=app_name_dict.values()
max_app=max(app)
min_app=min(app)
min_and_max = [max_app,min_app]
print(min_and_max)

plt.figure(figsize=(15,7))
plt.xlabel("Min-Max CPU Consumption")
plt.ylabel("Usage")
plt.bar(name_list, min_and_max,width=0.6,color=("red","blue"))
plt.show()