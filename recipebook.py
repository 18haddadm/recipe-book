items = 0

dict = {'Granulated Sugar':'1/2 cup',
'cinnamon':'1 teaspoon',
'biscuits':'2 cans',
'chopped walnuts':'1/2 cup',
'raisins':'1/2 cup',
'brown sugar':'1 cup',
'butter':'3/4 cup',
#'Step 1': 'Heat oven to 350°F. Lightly grease 12-cup fluted tube pan with shortening or cooking spray. In large -storage plastic food bag, mix granulated sugar and cinnamon',
#'Step 2':'Separate dough into 16 biscuits; cut each into quarters. Shake in bag to coat. Arrange in pan, adding walnuts and raisins among the biscuit pieces.',
#'Step 3':'In small bowl, mix brown sugar and butter; pour over biscuit pieces.',
#'Step 4':'Bake 30 to 35 minutes or until golden brown and no longer doughy in center. Cool in pan 10 minutes. Turn upside down onto serving plate; pull apart to serve. Serve warm.'
}

directions = ['Step 1: Heat oven to 350°F. Lightly grease 12-cup fluted tube pan with shortening or cooking spray. In large -storage plastic food bag, mix granulated sugar and cinnamon',
'Step 2: Separate dough into 16 biscuits; cut each into quarters. Shake in bag to coat. Arrange in pan, adding walnuts and raisins among the biscuit pieces.',
'Step 3: In small bowl, mix brown sugar and butter; pour over biscuit pieces.',
'Step 4: Bake 30 to 35 minutes or until golden brown and no longer doughy in center. Cool in pan 10 minutes. Turn upside down onto serving plate; pull apart to serve. Serve warm.']

#print ("Granulated Sugar:",dict['Granulated Sugar'])
#print ("cinnamon:",dict['cinnamon'])
#print ("biscuits:",dict['biscuits'])
#print ("chopped walnuts:",dict['chopped walnuts'])
#print ("raisins:",dict['raisins'])
#print ("brown sugar:",dict['brown sugar'])
#print ("butter:",dict['butter'])
#print ("Step 1:", dict['Step 1'])
#print ("Step 2:", dict['Step 2'])
#print ("Step 3:", dict['Step 3'])
#print ("Step 4:", dict['Step 4'])
for i in dict:
    print (i, dict[i])

for i in directions:
    print (directions[items])
    items +=1
