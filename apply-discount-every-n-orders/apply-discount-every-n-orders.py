class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.pp = defaultdict(int)
        for i in range(len(products)):
            self.pp[products[i]] = prices[i]
        self.count = 0
            

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count +=1
        bill = 0
        for i in range(len(product)):
            bill += self.pp[product[i]] * amount[i]
        if self.count%self.n==0:
            dis = (self.discount/100)*bill
            bill -= dis
        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)