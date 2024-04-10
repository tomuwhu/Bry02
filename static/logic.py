from browser import html as H, document as D, ajax as A

def q(req):
    for  e in req.json:
        D["x1"] <= H.B(e)

A.get("/data", oncomplete=q)

D["x1"] <= "Hello cica"

