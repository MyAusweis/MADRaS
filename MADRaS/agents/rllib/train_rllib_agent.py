import ray
import ray.rllib.agents.ppo as ppo
from ray.tune.logger import pretty_print
import MADRaS.rllib_helpers as helpers
import logging.config
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

helpers.register_madras()
ray.init()
config = ppo.DEFAULT_CONFIG.copy()
config["num_gpus"] = 0
config["num_workers"] = 1
config["eager"] = False


trainer = ppo.PPOTrainer(config=config, env="madras_env")

# Can optionally call trainer.restore(path) to load a checkpoint.

for i in range(10000):
   # Perform one iteration of training the policy with PPO
   result = trainer.train()
   print(pretty_print(result))

   if i % 10 == 0:
       checkpoint = trainer.save()
       logging.info("checkpoint saved at", checkpoint)