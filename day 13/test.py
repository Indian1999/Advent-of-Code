import pulp
def solve_eq(x, y, b, n = 0):
    lp = pulp.LpProblem("test", pulp.LpMinimize)

    x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
    x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")

    lp += x1 + 3*x2
    lp += x[0]*x1 + y[0]*x2 == b[0]#12748
    lp += x[1]*x1 + y[1]*x2 == b[1]#12176

    solver = pulp.PULP_CBC_CMD(msg=False)
    status = lp.solve(solver)

    if status == 1:
        modulo = (y[1]-(x[1]*y[0])/x[0])*x[0]
        
        return (pulp.value(x1), pulp.value(x2))
    else:
        return solve_eq(x, y, (b[0]+1,b[1]+1), n+1)
        """print("Optimal solution:")
        print(f"x1 = {pulp.value(x1)}")
        print(f"x2 = {pulp.value(x2)}")"""

print((8-(3*7)/5)*5) # This finds the modulo in which there is in integer solution
for i in range(200):
    result = solve_eq((5,3), (7,8), (22+i,19+i))
    if result[0].is_integer() and result[1].is_integer():
        print(f"i = {i};\t{result}")