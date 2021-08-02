from database import Database

data = Database("kaggle datasets download -d camnugent/california-housing-prices")

print(data.dataset)