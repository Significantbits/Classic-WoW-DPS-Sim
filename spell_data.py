# List is always cast_time,damage,dot,channel,mana,cool down,cool down flag, current cd time

# @TODO Need to add damage buff cool downs later like combustion

def create_spell_data():
    spell_data = {}

    # Mage damage spells
    spell_data['Fireball r1'] = [1.5,[14,23],(2.0/4.0),0,30,0,False,0]
    spell_data['Fireball r2'] = [2,[31,46],(3.0/6.0),0,45,0,False,0]
    spell_data['Fireball r3'] = [2.5,[53,74],(6.0/6.0),0,65,0,False,0]
    spell_data['Fireball r4'] = [3,[84,117],(12.0/8.0),0,95,0,False,0]
    spell_data['Fireball r5'] = [3.5,[139,188],(20.0/8.0),0,140,0,False,0]
    spell_data['Fireball r6'] = [3.5,[199,266],(28.0/8.0),0,185,0,False,0]
    spell_data['Fireball r7'] = [3.5,[255,336],(32.0/8.0),0,185,0,False,0]
    spell_data['Fireball r8'] = [3.5,[318,415],(40.0/8.0),0,260,0,False,0]
    spell_data['Fireball r9'] = [3.5,[392,507],(52.0/8.0),0,305,0,False,0]
    spell_data['Fireball r10'] = [3.5,[475,610],(60.0/8.0),0,350,0,False,0]
    spell_data['Fireball r11'] = [3.5,[561,716],(72.0/8.0),0,395,0,False,0]
    spell_data['Fire Blast r1'] = [0,[24,33],0,0,40,8,False,0]
    spell_data['Fire Blast r2'] = [0,[57,72],0,0,75,8,False,0]
    spell_data['Fire Blast r3'] = [0,[103,128],0,0,115,8,False,0]
    spell_data['Fire Blast r4'] = [0,[168,203],0,0,165,8,False,0]
    spell_data['Fire Blast r5'] = [0,[242,291],0,0,220,8,False,0]
    spell_data['Fire Blast r6'] = [0,[332,395],0,0,280,8,False,0]
    spell_data['Fire Blast r7'] = [0,[431,510],0,0,340,8,False,0]
    spell_data['Flamestrike r1'] = [3,[52,69],(48.0/8.0),0,195,12,False,0]
    spell_data['Flamestrike r2'] = [3,[96,123],(88.0/8.0),0,330,12,False,0]
    spell_data['Flamestrike r3'] = [3,[154,193],(140.0/8.0),0,490,12,False,0]
    spell_data['Flamestrike r4'] = [3,[220,273],(196.0/8.0),0,650,12,False,0]
    spell_data['Flamestrike r5'] = [3,[291,360],(264.0/8.0),0,815,12,False,0]
    spell_data['Flamestrike r6'] = [3,[375,460],(340.0/8.0),0,815,12,False,0]
    spell_data['Pyroblast r1'] = [6,[141,188],(56.0/12.0),0,125,0,False,0] # Dot stacks with Fireball?!?
    spell_data['Pyroblast r2'] = [6,[180,237],(72.0/12.0),0,150,0,False,0] # Dot stacks with Fireball?!?
    spell_data['Pyroblast r3'] = [6,[255,328],(96.0/12.0),0,195,0,False,0] # Dot stacks with Fireball?!?
    spell_data['Pyroblast r4'] = [6,[329,420],(124.0/12.0),0,240,0,False,0] # Dot stacks with Fireball?!?
    spell_data['Pyroblast r5'] = [6,[407,516],(156.0/12.0),0,285,0,False,0] # Dot stacks with Fireball?!?
    spell_data['Pyroblast r6'] = [6,[503,632],(188.0/12.0),0,335,0,False,0] # Dot stacks with Fireball?!?
    spell_data['Pyroblast r7'] = [6,[600,751],(228.0/12.0),0,385,0,False,0] # Dot stacks with Fireball?!?
    spell_data['Pyroblast r8'] = [6,[716,891],(268.0/12.0),0,440,0,False,0] # Dot stacks with Fireball?!?
    spell_data['Scorch r1'] = [1.5,[53,66],0,0,50,0,False,0]
    spell_data['Scorch r2'] = [1.5,[77,94],0,0,65,0,False,0]
    spell_data['Scorch r3'] = [1.5,[100,121],0,0,80,0,False,0]
    spell_data['Scorch r4'] = [1.5,[133,160],0,0,100,0,False,0]
    spell_data['Scorch r5'] = [1.5,[162,193],0,0,115,0,False,0]
    spell_data['Scorch r6'] = [1.5,[200,240],0,0,135,0,False,0]
    spell_data['Scorch r7'] = [1.5,[233,276],0,0,150,0,False,0]
    spell_data['Blast Wave r1'] = [0,[154,187],0,0,215,25,False,0]
    spell_data['Blast Wave r2'] = [0,[201,242],0,0,270,25,False,0]
    spell_data['Blast Wave r3'] = [0,[277,330],0,0,355,25,False,0]
    spell_data['Blast Wave r4'] = [0,[365,434],0,0,450,25,False,0]
    spell_data['Blast Wave r5'] = [0,[462,545],0,0,545,25,False,0]
    spell_data['Frostbolt r1'] = [1.5,[18,21],0,0,25,0,False,0]
    spell_data['Frostbolt r2'] = [1.8,[31,36],0,0,35,0,False,0]
    spell_data['Frostbolt r3'] = [2.2,[51,58],0,0,50,0,False,0]
    spell_data['Frostbolt r4'] = [2.6,[74,83],0,0,65,0,False,0]
    spell_data['Frostbolt r5'] = [3,[126,139],0,0,100,0,False,0]
    spell_data['Frostbolt r6'] = [3,[174,191],0,0,130,0,False,0]
    spell_data['Frostbolt r7'] = [3,[227,248],0,0,160,0,False,0]
    spell_data['Frostbolt r8'] = [3,[292,317],0,0,195,0,False,0]
    spell_data['Frostbolt r9'] = [3,[353,384],0,0,225,0,False,0]
    spell_data['Frostbolt r10'] = [3,[429,464],0,0,260,0,False,0]
    spell_data['Frostbolt r11'] = [3,[515,556],0,0,290,0,False,0]
    spell_data['Frost Nova r1'] = [0,[19,22],0,0,55,25,False,0]
    spell_data['Frost Nova r2'] = [0,[33,38],0,0,85,25,False,0]
    spell_data['Frost Nova r3'] = [0,[52,59],0,0,115,25,False,0]
    spell_data['Frost Nova r4'] = [0,[71,80],0,0,145,25,False,0]
    spell_data['Blizzard r1'] = [0,[200,200],0,(200.0/8.0),320,0,False,0] # Need to change damage, maybe make it damage per second
    spell_data['Blizzard r2'] = [0,[352,352],0,(352.0/8.0),520,0,False,0]
    spell_data['Blizzard r3'] = [0,[520,520],0,(520.0/8.0),720,0,False,0]
    spell_data['Blizzard r4'] = [0,[720,720],0,(720.0/8.0),935,0,False,0]
    spell_data['Blizzard r5'] = [0,[936,936],0,(936.0/8.0),1160,0,False,0]
    spell_data['Blizzard r6'] = [0,[1192,1192],0,(1192.0/8.0),1400,0,False,0]
    spell_data['Cone of Cold r1'] = [0,[98,109],0,0,210,12,False,0]
    spell_data['Cone of Cold r2'] = [0,[146,161],0,0,290,12,False,0]
    spell_data['Cone of Cold r3'] = [0,[203,224],0,0,380,12,False,0]
    spell_data['Cone of Cold r4'] = [0,[264,291],0,0,465,12,False,0]
    spell_data['Cone of Cold r5'] = [0,[335,366],0,0,555,12,False,0]
    spell_data['Arcane Missiles r1'] = [0,[24,24],0,3,85,0,False,0]
    spell_data['Arcane Missiles r2'] = [0,[36,36],0,4,140,0,False,0]
    spell_data['Arcane Missiles r3'] = [0,[56,56],0,5,235,0,False,0]
    spell_data['Arcane Missiles r4'] = [0,[83,83],0,5,320,0,False,0]
    spell_data['Arcane Missiles r5'] = [0,[115,115],0,5,410,0,False,0]
    spell_data['Arcane Missiles r6'] = [0,[151,151],0,5,500,0,False,0]
    spell_data['Arcane Missiles r7'] = [0,[192,192],0,5,595,0,False,0]
    spell_data['Arcane Missiles r8'] = [0,[230,230],0,5,655,0,False,0]
    spell_data['Arcane Explosion r1'] = [0,[32,37],0,0,75,0,False,0]
    spell_data['Arcane Explosion r2'] = [0,[57,64],0,0,120,0,False,0]
    spell_data['Arcane Explosion r3'] = [0,[97,106],0,0,185,0,False,0]
    spell_data['Arcane Explosion r4'] = [0,[139,152],0,0,250,0,False,0]
    spell_data['Arcane Explosion r5'] = [0,[186,203],0,0,315,0,False,0]
    spell_data['Arcane Explosion r6'] = [0,[243,264],0,0,390,0,False,0]
    
    return spell_data

