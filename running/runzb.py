from main import multicast_province
config_files = ["data/湖北电信_config.txt", "data/四川电信_config.txt"]
for config_file in config_files:
    multicast_province(config_file)
print(f"组播地址获取完成")
