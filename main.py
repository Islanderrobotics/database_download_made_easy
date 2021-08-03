from database import Database

data = Database("kaggle datasets download -d camnugent/california-housing-prices")

for i in data.dataset:
    print(i)