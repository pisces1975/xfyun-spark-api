# from spark_speaker import SparkSpeaker
from spark_gpt import SparkGPT
import time
from questions import q_writeCode1,q_business,q_explainCode_pom,q_explainCode_python,q_transaltion,q_writeCode2

# 1. 直接实例化SparkSpeaker即可，实例化时可以传入一个prompt
# speaker = SparkSpeaker("接下来我会给你发送一个文案，请你以伴侣的口吻帮我润色一下，加上合适的称呼")
speaker = SparkGPT("请如实回答问题，谢谢")
search_latency_fmt = "->-> search latency = {:.4f}s"

print("Start to ask...")
time_1 = time.time()  
# 2. 单次询问
answer = speaker.ask(q_explainCode_pom)
time_2 = time.time()  
 
print(answer)
print(f"->->-> Token used: {speaker.get_tokens()}, cost is {speaker.get_cost()}")
print(search_latency_fmt.format(time_2 - time_1))  
# 输出示例：
# 亲爱的，我知道我们的相遇是缘分所赐，而能够和你在一起，每一分、每一秒都是我今生今世的幸福。这份幸福，是我一生最珍贵的宝藏。
# 谢谢你为我带来的一切美好，我愿意与你一起，永远珍惜这份恩赐的福祉。

# speaker.ask("今生今世有缘和你在一起，每一分，每一秒都是幸福，都是老天恩赐的福祉。", flow_print=True)
# ask方法也可传入一个flow_print参数，值为True或False。该值为True时，系统会在终端窗口流式打印接收到的回应


# # 3. 多轮对话
# speaker.talk()

# print(speaker.text)  # text中，存放了会话记录
