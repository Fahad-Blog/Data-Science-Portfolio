import pandas as pd
import numpy as np

def generate_play_store_data(size=1000):
    np.random.seed(42)
    
    data = {
        'Category': np.random.choice(['Game', 'Tools', 'Finance', 'Social', 'Productivity'], size),
        'Review_Count': np.random.randint(10, 50000, size),
        'Size_MB': np.random.uniform(2, 200, size),
        'Price': np.random.choice([0, 0.99, 2.99, 9.99], size, p=[0.7, 0.15, 0.1, 0.05]),
        'Rating': np.random.uniform(1, 5, size)
    }
    
    df = pd.DataFrame(data)
    
    # Let's add "Logic" so the model actually works:
    # 1. Apps with more reviews tend to have higher ratings
    # 2. Very expensive apps tend to have slightly lower ratings (users are pickier)
    df['Rating'] = (df['Rating'] + (df['Review_Count'] / 10000) - (df['Price'] / 10)).clip(1, 5)
    
    return df

# Create it
df_google = generate_play_store_data()
print(df_google.head())
