'''
symbol = []
name = []
atomic_number = []
group = []
period = []
relative_atomic_mess = []
electron_shell = []
'''
print('--------------------元素周期表查找器 v3.7.1Alpha--------------------')
print("\n这个程序可以帮助你快速的找到一个化学元素或根离子的简要参数\n目前支持五种服务模式 (S\\A\\I\\Q\\T):\n\
    \nS:这是符号与名称搜索方式, 如果键入‘O’或者‘oxygen’（只能输入英文名）, 便会展示氧元素的简要信息.\
    \nA:这是原子序数搜索模式. 例如, 如果你键入‘2’它便会展示周期表中第二个元素的简要信息\
    \nI:这是根离子查找模式，你可以输入一个根离子的化学符号或英文全名(不带化合价)\n  便会显示你输入的根离子的信息\
    \nQ:这个模式是退出模式，你要是选了这个，那这个程序就被关掉了\nT:如果你想反馈信息错误或程序漏洞，那就选择这个\
    \nPs:元素符号的第一个字母必须大写, 元素英文名的每个字母必须小写.\n   根离子的化学符号的每个字母必须是大写,根离子英文名的首字母必须大写.\n   如果不遵循以上所有原则，那么可能不能达到你的预期目的" + '\n')

big_list = [['H','hydrogen','1','1','1','1.0','1'],\
    ['He','helium','2','1','18','4.0','2'],\
    ['Li','lithium','3','1','2','6.9','2.1'],\
    ['Be','beryllium','4','2','2','9.0','2.2'],\
    ['B','boron','5','13','2','10.8','2.3'],\
    ['C','carbon','6','14','2','12','2.4'],\
    ['N','nitrogen','7','15','2','14.0','2.5'],\
    ['O','oxygen','8','16','2','16.0','2.6'],\
    ['F','fluorine','9','17','2','19.0','2.7'],\
    ['Ne','neon','10','18','2','20.2','2.8'],\
    ['Na','sodium','11','1','3','23.0','2.8.1'],\
    ['Mg','magnesium','12','2','3','24.3','2.8.2'],\
    ['Al','aluminium','13','13','3','26.982','2.8.3'],\
    ['Si','silicon','14','14','3','28.1','2.8.4'],\
    ['P','phosphorus','15','15','3','31.0','2.8.5'],\
    ['S','sulfur','16','16','3','32.1','2.8.6'],\
    ['Cl','chlorine','17','17','3','35.5','2.8.7'],\
    ['Ar','argon','18','18','3','39.9','2.8.8'],\
    ['K','potassium','19','1','4','39.1','2.8.8.1'],\
    ['Ca','calcium','20','2','4','40.1','2.8.8.2'],\
    ['Sc','scandium','21','3','4','45.0','2.8.8.3'],\
    ['Ti','titanium','22','4','4','47.9','2.8.8.4'],\
    ['V','vanadium','23','5','4','50.9','2.8.8.5'],\
    ['Cr','chromium','24','6','4','52.0','2.8.8.6'],\
    ['Mn','manganese','25','7','4','54.9','2.8.8.7'],\
    ['Fe','iron','26','8','4','55.8','2.8.8.8'],\
    ['Co','cobalt','27','9','4','58.9'],\
    ['Ni','nickel','28','10','4','58.7'],\
    ['Cu','copper','29','11','4','63.5'],\
    ['Zn', 'zinc', '30','12','4','65.409'],\
    ['Ga', 'gallium','31','13','4','69.723'],\
    ['Ge','germanium','32','14','4','72.64'],\
    ['As','arsenic','33','15','4','74.9'],\
    ['Se','selenium','34','16','4','79.0'],\
    ['Br','bromine','35','17','4','79.9'],\
    ['Kr','krypton','36','18','4','83.8'],\
    ['Rb','rubidium','37','1','5','85.5'],\
    ['Sr','strontium','38','2','5','87.6'],\
    ['Y','yttrium','39','3','5','88.9'],\
    ['Zr','zirconium','40','4','5','91.2'],\
    ['Nb','niobium','41','5','5','92.9'],\
    ['Mo','molybdenum','42','6','5','96.0'],\
    ['Tc','technetium','43','7','5','98'],\
    ['Ru','ruthenium','44','8','5','101.1'],\
    ['Rh','rhodium','45','9','5','102.9'],\
    ['Pd','palladium','46','10','5','106.4'],\
    ['Ag','silver','47','11','5','107.9'],\
    ['Cd','cadmium','48','12','5','112.4'],\
    ['In','indium','49','13','5','114.8'],\
    ['Sn','tin','50','14','5','118.7'],\
    ['Sb','antimony','51','15','5','121.8'],\
    ['Te','tellurium','52','16','5','127.6'],\
    ['I','iodine','53','17','5','126.9'],\
    ['Xe','xenon','54','18','5','131.3'],\
    ['Cs','caesium','55','1','6','132.9'],\
    ['Ba','barium','56','2','6','137.3'],\
    ['La','lanthanum','57','3','6','138.9'],\
    ['Ce','cerium','58','6','140.1'],\
    ['Pr','praseodymium','59','3','6','140.9'],\
    ['Nd','neodymium','60','3','6','144.2'],\
    ['Pm','promethium','61','3','6','145'],\
    ['Sm','samarium','62','3','6','150.4'],\
    ['Eu','europium','63','3','6','152.0'],\
    ['Gd','gadolinium','64','3','6','157.3'],\
    ['Tb','terbium','65','3','6','158.9'],\
    ['Dy','dysprosium','66','3','6','162.5'],\
    ['Ho','holmium','67','3','6','164.9'],\
    ['Er','erbium','68','3','6','167.3'],\
    ['Tm','thulium','69','3','6','168.9'],\
    ['Yb','ytterbium','70','3','6','173.1'],\
    ['Lu','lutetium','71','3','6','175.0'],\
    ['Hf','hafnium','72','4','6','178.5'],\
    ['Ta','tantalum','73','5','6','180.9'],\
    ['W','tungsten','74','6','6','183.8'],\
    ['Re','rhenium','75','7','6','186.2'],\
    ['Os','osmium','76','8','6','190.2'],\
    ['Ir','iridium','77','9','6','192.2'],\
    ['Pt','platinum','78','10','6','195.1'],\
    ['Au','gold','79','11','6','197.0'],\
    ['Hg','mercury','80','12','6','200.6'],\
    ['Tl','thallium','81','13','6','204.4'],\
    ['Pb','lead','82','14','6','207.2'],\
    ['Bi','bismuth','83','15','6','209.0'],\
    ['Po','polonium','84','16','6','210'],\
    ['At','astatine','85','17','6','210'],\
    ['Rn','radon','86','18','6','222'],\
    ['Fr','francium','87','1','7','223'],\
    ['Ra','radium','88','2','7','226'],\
    ['Ac','actinium','89','3','7','227'],\
    ['Th','thorium','90','3','7','232.0'],\
    ['Pa','protactinium','91','3','7','231.0'],\
    ['U','uranium','92','3','7','238.0'],\
    ['Np','neptunium','93','3','7','237'],\
    ['Pu','plutonium','94','3','7','244'],\
    ['Am','americium','95','3','7','243'],\
    ['Cm','curium','96','3','7','247'],\
    ['Bk','berkelium','97','3','7','247'],\
    ['Cf','californium','98','3','7','251'],\
    ['Es','einsteinium','99','3','7','252'],\
    ['Fm','fermium','100','3','7','257'],\
    ['Md','mendelevium','101','3','7','258'],\
    ['No','nobelium','102','3','7','259'],\
    ['Lr','lawrencium','103','3','7','262'],\
    ['Rf','rutherfordium','104','4','7','261'],\
    ['Db','dubnium','105','5','7','262'],\
    ['Sg','seaborgium','106','6','7','266'],\
    ['Bh','bohrium','107','7','7','264'],\
    ['Hs','hassium','108','8','7','267'],\
    ['Mt','meitnerium','109','9','7','268'],\
    ['Ds','darmstadtium','110','10','7','271'],\
    ['Rg','roentgenium','111','11','7','272'],\
    ['Cn','copernicium','112','12','7','285'],\
    ['Nh','nihonium','113','13','7','280'],\
    ['Fl','flerovium','114','14','7','289'],\
    ['Mc','moscovium','115','15','7','289'],\
    ['Lv','livermorium','116','16','7','292'],\
    ['Ts','tennessine','117','17','7','294',],\
    ['Og','oganesson','118','18','7','294']]

ions_list = [['Lithium', 'Li', '1+'],\
    ['Sodium', 'Na', '1+'],\
    ['Potassium', 'K', '1+'],\
    ['Hydrogen', '  H', '1+'],\
    ['Copper(I)', 'Cu', '1+'],\
    ['Silver', 'Ag', '1+'],\
    ['Ammonium', 'NH4', '1+'],\
    ['Hydronium', 'H3O', '1+'],\
    ['Magnesium', 'Mg', '2+'],\
    ['Calcium', 'Ca', '2+'],\
    ['Strontium', 'Sr', '2+'],\
    ['Barium', 'Ba', '2+'],\
    ['Iron(III)', 'Fe', '3+'],\
    ['Copper', 'Cu', '2+'],\
    ['Zinc', 'Zn', '2+'],\
    ['Lead', 'Pb', '2+'],\
    ['Aluminium', 'Al', '3+'],\
    ['Chromium(III)', 'Cr', '3+'],\
    ['Iron(II)', 'Fe', '2+'],\
    ['Tin(IV)', 'Sn', '4+'],\
    ['Lead(IV)', 'Pb', '4+'],\
    ['Fluoride', 'F', '1-'],\
    ['Chloride', 'Cl', '1-'],\
    ['Bromide', 'Br', '1-'],\
    ['Iodide', 'I', '1-'],\
    ['Hydroxide', 'OH', '1-'],\
    ['Nitrate', 'NO3', '1-'],
    ['Permanganate', 'MnO4', '1-'],\
    ['Cyanide', 'CN', '1-'],\
    ['Hydrogen sulfate', 'HSO4', '1-'],\
    ['Hydrogen carbonate', 'HCO3', '1-'],\
    ['Ethanoate ion', 'CH3COO', '1-'],\
    ['Oxide', 'O', '2-'],\
    ['Sulfate', 'SO4', '2-'],\
    ['Sulfide', 'S', '2-'],\
    ['Carbonate', 'CO3', '2-'],\
    ['Chromate', 'CrO4', '2-'],\
    ['Dichromate', 'Cr2O7', '2-'],\
    ['Thiosulfate', 'S2O3', '2-'],\
    ['Nitride', 'N', '3-'],\
    ['Phosphate', 'PO4', '3-']]

def search():
    global big_list
    
    info = input('>>>')
    if info.lower() == 'quit':
        return 'quit'
    
    for small_list in big_list:
        if info in small_list:
            return small_list
    
    return 'Element cannot find.'

def atomic_number_search():
    global big_list
    
    info = input('>>>')
    if info.lower() == 'quit':
        return 'quit'
    try:
        info = int(info)
    except:
        return 'The atomic number is not valid'
    else:
        if info > 0 and info < 119 and info % 1 == 0:
            for small_list in big_list:
                if str(info) == small_list[2]:
                    return small_list
    
    return 'Element cannot find.'

def ion_search():
    global ions_list
    info = input('>>>')
    if info.lower() == 'quit':
        return 'quit'

    gay = []
    for ion in ions_list:
        if info in ion:
            gay.append(ion)
    return gay

active = True
while active:
    chose = input('选择一个模式：元素名称或符号搜索\\原子序数搜索\\根离子搜索\\退出\\反馈错误与意见 (S\\A\\I\\Q\\T)\n>>>')
    if chose.lower() == 'q':
        active = False
    
    elif chose.lower() == 's':
        print("---元素名称或符号搜索(键入'quit'以重新选择模式)---")
        while True:
            element = search()
            if element == 'Element cannot find.':
                print("元素不存在或未被发现")
            elif element == 'quit':
                break
            else:
                print('--------------------')
                print('符号     :',element[0])
                print('英文名称 :',element[1])
                print('原子序数 :',element[2])
                print('质量     :',element[5])
                print('族',element[3],', 周期',element[4])
                print('--------------------')
    
    elif chose.lower() == 'a':
        print("---原子序数搜索（键入'quit'以重新选择模式）---")
        while True:
            element = atomic_number_search()
            if element == 'Element cannot find.':
                print("元素不存在或未被发现")
            elif element == 'The atomic number is not valid':
            	print('键入的原子序数无效')
            elif element == 'quit':
                break
            else:
                print('--------------------')
                print('符号       :',element[0])
                print('英文名称   :',element[1])
                print('原子序数   :',element[2])
                print('质量       :',element[5])
                print('族',element[3],', 周期',element[4])
                print('--------------------')

    elif chose.lower() == 'i':
        print("---原子序数搜索（键入'quit'以重新选择模式）---")
        while True:
            ion = ion_search()
            if ion == 'quit':
                break
            else:
                if ion:
                    for g in ion:
                        print('--------------------')
                        print('根离子英文名称   :',g[0])
                        print('符号            :',g[1])
                        print('化合价          :',g[2])
                        print('--------------------')
                else:
                    print('此根离子暂未被录入')

    elif chose.lower() == 't':
    	print("此程序目前处于测试阶段,所以可能存在BUG或化学元素信息错误.\n当你发现问题想要提意见, 有新的想法或者感到无聊时:\
    	\n请在QQ中搜索2844933250(这是作者QQ)或找到作者本人与其面谈,\
    	\n随后有概率会发布错误被修复的新版本.\n")
    
    else:
        print('暂不支持此功能')
