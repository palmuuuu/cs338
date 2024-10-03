import math
import sympy

e = 65537
d = int("44370256056956057162247355539033835202771725129817113556071455357563847182847509068"
        "37808638124926896930295389206508634085634897045175108731106395698961384866042572078"
        "58578197327855530786899764569401782035712361467732615431271616732220087750028551636"
        "83442295740828479837591554591067315085802447454155595933884615258868619088995861109"
        "75936329892287114184902693718815229900018767754201535458312900685275148657910141566"
        "00123056294125908832436359735872174897164106834474936511926388174551878553066434084"
        "49973370765146383649867267789945631349033649010896162209899083372440609003136862752"
        "65141802052028660075141330800869633938979513307021825190387683123430350347399109682"
        "67196173343203206105707718735861568124209307638577002044722172842854807182300671877"
        "36558990449953413000506781883576508926950137931360962820291117127120656735605902713"
        "43886711089564905523908184276149061915227274388928110619136444284329845043066477517"
        "378950944329")

prime1 = int("232646930022035812150226807722563972011819587886585819999472185001287487719088309179"
             "434083156592257695976168035910549281687132756776062370698577983612893386939089736526"
             "768055944222977167151994575190116894535437670757147004673803762878896804631501038263"
             "421149917610381821656108906728020981200715408196050656851064313429594275654525172549"
             "425715385641252818743504192965646717185721672885773790011531314373812684788513008495"
             "1998739476965860209888259913062118498624093")

prime2 = int("192986702402193974690687396567723750123474649154939460405388037631116172170488679599"
             "228669501967288336040908974295007050428387153946209485834638280755193679040486554505"
             "884939168225249939964051076570197847795152731106890341124057617662814737934220822640"
             "590505629460575607973756290084616837469416734768173511728179265222045127903623891702"
             "967713942518706358624170916713230596448331042072267582332955263671043516160504799186"
             "5463820159138119402976229920011275851477699")


lambda_n = sympy.lcm(prime1 - 1, prime2 - 1)

check = (e * d) % lambda_n

print(f"lambda(n): {lambda_n}")
print(f"(e * d) % lambda(n): {check}")
print("Does (e * d) % lambda(n) == 1? ", check == 1)
