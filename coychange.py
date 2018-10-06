def create(self, validated_data):
        bill= validated_data['bill']
        amount = validated_data['amount']
        change = amount-bill
        get = change
        ram=Inventory.objects.filter(id=1).first()
        b=model_to_dict(ram)
        print("getting:",b)
        l=[]
        k=b.keys()
        print(k)
        v=b.values()
        print(v)
        h=Inventory.objects.filter(id=2).first()
        g=model_to_dict(h)
        f={key:values for key,values in g.items() if key!='id' }
        print("delate:",f)
        inv=[re.findall(r'(\w+?)(\d+)', key)[0] for key,values in g.items() if key!='id']
        print("inverse",inv)
        mon=[]
        z=f.values()
        print(z)
        for u,x in inv:
            mon.append(int(x))
        print("fuc:",(mon))
        dic=dict(zip(mon,z))
        print("zero:",dic)
        d=[re.findall(r'(\w+?)(\d+)', key)[0] for key,values in b.items() if key!='id']
        print("fsfsbhdf:",d)
        for w,q in d:
            l.append(int(q))
        denoms=sorted(l,reverse=True)
        print("denoms:",denoms)
        for i in denoms:
            if b[i]>0:
                while (get >= i and b[i]>0):
                        num = get // denoms[i]
                        get -= (num * denoms[i])
                        dec={denoms[i]:num}
                        dic.update(dec)
                        print("bjbdfb:",dic)
        denoms = denoms[1:]
        obj = Bill(bill=bill, amount=amount,change=change,Rs2000=dic[2000],Rs500=dic[500],Rs200=dic[200],Rs100=dic[100],Rs50=dic[50],Rs10=dic[10],Rs5=dic[5],Rs2=dic[2],Rs1=dic[1])
        obj.save()
        q=model_to_dict(obj)
        v=dict(Counter(b)-Counter(q))
        x =InventorySerializer(ram,data=v)
        if x.is_valid():
            x.save()
        return obj

