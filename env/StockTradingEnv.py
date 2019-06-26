import gym
from gym import spaces

class StockTradingEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self, arg1, arg2):
    super(StockTradingEnv, self).__init__()
    self.df = df
    self.reward_range = (0, MAX_ACCOUNT_BALANCE)

    # Actions of the format Buy x%, Sell x%, Hold, etc.
    self.action_space = spaces.Box(
      low=np.array([0, 0]), high=np.array([3, 1]), dtype=np.float16)

    # Prices contains the OHCL values for the last five prices
    self.observation_space = spaces.Box(
      low=0, high=1, shape=(6, 6), dtype=np.float16)

  def step(self, action):
    # Execute one time step within the environment
    ...
  def reset(self):
    # Reset the state of the environment to an initial state
    self.balance = INITIAL_ACCOUNT_BALANCE
    self.net_worth = INITIAL_ACCOUNT_BALANCE
    self.max_net_worth = INITIAL_ACCOUNT_BALANCE
    self.shares_held = 0
    self.cost_basis = 0
    self.total_shares_sold = 0
    self.total_sales_value = 0
 
  # Set the current step to a random point within the data frame
  self.current_step = random.randint(0, len(self.df.loc[:, 'Open'].values) - 6)
  return self._next_observation() 
     ...
  def render(self, mode='human', close=False):
    # Render the environment to the screen
    ...
