from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter

agent = Agent.load("/home/lilbill/rasa/models/nlu-20200417-023249.tar.gz")
agent.handle_text("hello")
