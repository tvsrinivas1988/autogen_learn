import asyncio
from autogen_agentchat.agents import CodeExecutorAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

async def main():
    docker = DockerCommandLineCodeExecutor(
        work_dir='tmp',
        timeout=120
    )

    code_executor_agent = CodeExecutorAgent(
        name='code_executor_agent',
        code_executor = docker
    )

    task = TextMessage(content='''
                       Here is the code 
```python
print("Hello World!")
```
                       ''',
                       source='user')
    
    await docker.start()
    result = await code_executor_agent.on_messages(
        messages=[task],
        cancellation_token =CancellationToken()
    )

    print("The result is :" , result)

    await docker.stop()

if __name__ == "__main__":
    asyncio.run(main())    