para_1="The quick brown fox jumps over a lazy dog"
para_2="a dog fox jumps over the lazy quick brown"
para_3="he lazy quick brown dog jumps over a lazy fox dog"

paragraphs_combined= (para_1+" "+ para_2+ " "+para_3).lower()
lst_c=set(paragraphs_combined.split(' '))
lst_1=(para_1.split(' '))
lst_2=(para_2.split(' '))
lst_3=(para_3.split(' '))

vector1=[]
for i in lst_c:
  counter=0
  for j in lst_1:
    if i==j:
      counter+=1
  vector1.append(counter)
vector2=[]
for i in lst_c:
  counter=0
  for j in lst_2:
    if i==j:
      counter+=1
  vector2.append(counter)
vector3=[]
for i in lst_c:
  counter=0
  for j in lst_3:
    if i==j:
      counter+=1
  vector3.append(counter)

def cos (v1, v2):
  l1=len(v1)
  l2=len(v2)
#top part
  dot=0
#bottom part
  A2=0
  B2=0
  for i in range(len(v1)):
    dot+=v1[i]*v2[i]
    A2+=v1[i]*v1[i]
    B2+=v2[i]*v2[i]
  A2=A2**0.5
  B2=B2**0.5
  return (dot/(A2*B2))

print(cos(vector1,vector2))
print(cos(vector1,vector3))
print(cos(vector2,vector3))