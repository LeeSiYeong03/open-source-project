#List ������ Ȯ���ϱ�
a = [10, 20, 30, 40, 50]
print(a)

#�� ����Ʈ �����
a = []
print(a)

#List�� �ֿ� �޼ҵ�
append() = ����Ʈ �������� element �߰�
insert() = ������ index ��ġ�� element�� �߰�
remove() = ������ element ����Ʈ���� ����
del = ����Ʈ���� �����ϰ� ���� �׸��� index number�� �˰� �ִ� ��� del ���
pop() = ����Ʈ���� ������ �׸��� �����ϰų�, ��ȣ �ȿ� �ε����� �Է��Ͽ� Ư�� �׸� ����
len() = ����Ʈ�� ���Ե� element�� ���� ǥ��

#�޼ҵ� example
�湮�ϰ� ���� ����� "bucketList"�� ����� �Ʒ� ������ ���Ͻÿ�.
bucketList = ['����', '�뱸', '�λ�']

adding ���� the end of the List = bucketList.append('����')
printing the length of List = len(bucketList)
adding ���� in the index 1 = bucketList.insert(1, '����')
removing ���� in the List = bucketList.remove('����') or del bucketList[0]
removing the last element in the List = bucketList.pop()
clear every element in the List = bucketList.clear()

#slice
slice = ���� ������ ���� index, ���� index, ���� ������ �� ����
example = Listname[0,6,2] = 0 (����), 6 (��), 2 (����(����, ����))

bucketList = ['�谡õ', '22', '����', '����', '�λ�', '����']
bucketList [0:6:2]
['�谡õ', '����','�λ�']
bucketList[2:6] = print index 2 to index 5
bucketList[3:] = print indext 3 to the end
bucketList[:3] = print indext 0 to index 2

#Negative indexing
���� �ε��� = python sequence �ڷ� ������ �����ϴ� ��� element�� ���� �׼��� ���
- index -1 = access of the last element in the List. my_list[-1]
- index -2 = access of the second element from the bottom of the List. my_list[-2]

#���ڿ� slice
a = "Life is too short, you need python"

a[0] = L, a[1] = i, a[2] = f, a[3] = e
a[0:4] =Life

a[-6:] = �ڿ��� 6����, �� p���� ������ = python

#����Ʈ ����
���� (Concentration): '+' �����ڸ� ����Ͽ� �� ����Ʈ�� ����
�ݺ� (Repetition): '*' �����ڸ� ����Ͽ� ������ Ƚ�� ��ũ ����Ʈ ��� �ݺ�

���� �� �ݺ� ����: 
goodplace = ['Rome', 'Seoul']
city = ['Tokyo', 'Beijing']

goodplace + city = ['Rome', 'Seoul', 'Tokyo', 'Beijing'] = ����
city*3 = ['Tokyo', 'Beijing', 'Tokyo', 'Beijing', 'Tokyo', 'Beijing'] = �ݺ�


