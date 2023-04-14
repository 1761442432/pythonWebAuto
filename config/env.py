
env_dict = {
    "dev" : "https://www.baidu.com",
    "test" : "https://www.jd.com",
    "pro" : "https:///www.taobao.com"
}
if __name__ == '__main__':
    current_url = "pro"
    print(env_dict[current_url])