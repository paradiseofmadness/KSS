def klammern(f:str):
    x=f.split('*')
    if len(x)==1:
        return [f'{f}']
    res = []
    for i in range(1, len(x)):
        res1=klammern('*'.join(x[:i]))
        res2=klammern('*'.join(x[i:]))
        for ii in res1:
            for iii in res2:
                res.append(f'({ii}*{iii})')
    return res

if __name__ == "__main__":
  for k in klammern("x1*x2*x3*x4"):
      print(k)