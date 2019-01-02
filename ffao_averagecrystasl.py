x = ['lacked',"ifever","dosing","barred","bikini","mildly","waiter","purist"]
for a in range(6):
    print(a)
    for i in range(1,256):
        st = []
        sm = 0
        ct = 0
        for j in range(8):
            if (i>>j)%2 == 1:
                sm += ord(x[j][a])
                ct += 1
                st.append(x[j])
        if sm/ct == ord('haloes'[a]): print(st)
