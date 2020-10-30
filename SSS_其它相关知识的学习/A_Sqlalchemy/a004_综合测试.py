from SSS_其它相关知识的学习.A_Sqlalchemy.models import GUOJIA, Qiangxie, DB

cli_session = DB()

# china = GUOJIA(name='中国')
# usa = GUOJIA(name='美利坚')
#
# a95 = Qiangxie(name='95式自动步枪', GUOJIA_id=1)
# a56 = Qiangxie(name='56式冲锋枪', GUOJIA_id=1)
# a81 = Qiangxie(name='81式步枪', GUOJIA_id=1)
# M16 = Qiangxie(name="M16制式步枪", GUOJIA_id=2)
# AR = Qiangxie(name='AR15步枪', GUOJIA_id=2)
#
# cli_session.add_all([china, usa, a56,a81,a95,M16,AR])
# cli_session.commit()

#
for i in cli_session.query(GUOJIA).all():
    print(i.name," :", i.Qiangxie)
    #中国  : [枪械:56式冲锋枪, 枪械:81式步枪, 枪械:95式自动步枪]
    #美利坚  : [枪械:M16制式步枪, 枪械:AR15步枪]

a,b = (cli_session.query(Qiangxie).first(), cli_session.query(Qiangxie).all()[-1])
print(a, a.GUOJIA)#枪械:56式冲锋枪 国家:中国
print(b, b.GUOJIA)#枪械:AR15步枪 国家:美利坚

print(b.GUOJIA.Qiangxie)#[枪械:M16制式步枪, 枪械:AR15步枪]
print(b.GUOJIA.Qiangxie[0].GUOJIA)#国家:美利坚
#老套娃了

cli_session.close()




