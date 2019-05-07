# Python ile Kriptografi Algoritmaları

- Ceaser Chiper Algorithm (Sezar Şifreleme Algoritması)
- Matris Şifreleme Algoritması

------------


## Ceaser Chiper Algorithm (Sezar Şifreleme Algoritması)

Türkçe karşılığı Sezar Şifreleme olan bu algoritma adından da anlaşılacağı üzere Jul Sezar tarafından oluşturulmuştur.Jul Sezar mesajlarının düşmanlarının eline geçirilebileceği tehlikesini düşünerek mesajlarında bu yöntemi kullanmıştır.Bu algoritma şifreleme algoritmalarının en çok bilinen ve kullanılan yöntemlerinden birisidir. Bu şifreleme yöntemi ile şifrelenmiş mesajlar , konuya hakim olmayan biri tarafından okunulduğu zaman gerçekten bir şey ifade etmeyecektir fakat konuya hakim olan birisi tarafından mesajın şifrelendiği algoritmanın Sezar şifreleme yöntemi olduğunu anlaması sadece bir kaç dakikasını alacaktır. Bu yönden basitlik tarafından algoritmayı yazmak ve mesajları şifrelemek hızlı fakat yine aynı basitlikten dolayı siber dünyada güçsüz bir algoritmadır.

#### Peki Sezar Şifrelem Algoritması nasıl çalışır ? 

Sezar şifreleme algoritmasının çalışma yapısı oldukça basittir.Sezar algoritması mesajın her bir harfini belirtilen anahtar sayı kadar ileri kaydırarak şifreli mesajı oluşturur.

![Sezar Şifreleme (Ceaser Chiper)](https://cdn-images-1.medium.com/max/1600/1*I8BRRDM6HRBHjeExZ-sw-Q.jpeg "Sezar Şifreleme (Ceaser Chiper)")

Şifreyi çözmek için ise anahtar sayısı ile şifreli mesajdaki her karakterin anahtar sayısı kadar geriye giderek ana mesajı dönüştürülmesi üzerinedir.


# Matris Şifreleme Algoritması

Öncelikle bu algoritmanın nereden geldiği ve kim tarafından üretildiğini bilmemekle beraber internette kriptografi ile ilgili araştırma yaptığım sırada denk geldiğim bir video ve forum yazısından dikkatimi çekti. Açıkcası algoritmanın Hill algoritmasına benzediğini söylersek çok da yanlış olmayacaktır.

Algoritmada beni en çok etkileyen ve heyecanlandıran altında yatan matematik oldu.Lafı çok uzatmadan algoritmanın çalışma sistemine geçelim.

### Matris Şifreleme Algoritması nasıl çalışır ? 

#### Şİfreleme İşlemi :

Öncelikle ;

![](https://cdn-images-1.medium.com/max/800/1*pLPeNbdE7fKRrF_6kK9VXQ.png)

Böyle bir tablomuz olduğunu düşünelim ve her karakteri 10'luk tabanda bir sayıya eşitleyelim.

Eğer bu tablo yardımıyla DEGERR yazmak istersek ;

68 69 71 69 82 82  gibi bir sayı kümesi elde ediyoruz.Bu sayı kümesini 2x3 'lük matrise çeviriyoruz.

**Bu matris artık bizim şifresiz matrisimiz**  
          68 69 71
          69 82 82 

Daha sonrasında matrisi iyice karıştırmak için 2x2'lik anahtar matrisi yaratıyoruz. Matrislerin boyutlarını neden böyle seçtiğimi ilerleyen başlıklarda anlatacağım...

 **Anahtar Matris**  x **Şifresiz Matris** = **Şifreli Matris**
 
 1 9       68 69 71      689	807	809
 2 3   x   69 82 82   =  343	384	388
 

İşleri biraz daha karıştırmak amacıyla Anahtar matris ile Şifresiz Matris'i çarpıyoruz.


**Şifreli Matris** 

689	807	809
343	384	388


Şifreli matris artık mesajımızın son hali. Şifresiz matriste aynı olan harfler bile şifreli matriste birbirlerinden alakasız sayılara dönüşüyorlar. Matris şifrelemenin en güzel yanlarından birisi de bu.


#### Şifre Çözme İşlemi 

Şifre çözme işleminde ise yine matris kurallarına başvuruyoruz.

Matris kurallarını hatırlayacak olursak ;


A = Anahtar Matris![](https://i.hizliresim.com/r5AdmV.png)
B = Şifresiz Matris ![](https://i.hizliresim.com/dv1qW7.png)
C = Şifreli Matris  ![](https://i.hizliresim.com/8aVE9A.png)

**A** X **B** = **C** ise ;

 ![](https://hizliresim.com/MVOl62)
**A'nın Tersi** x **Şifreli Matris** = **Şifresiz Matris**

Denklemini elde ederiz ve bu sayede şifre çözme işlemini gerçekleştiririz.

#### Neden 2x2 ve 2x3 Matrisler ?

Bu algoritma için karşımıza çıkan bir kaç matematiksel zorluk var:

1. Anahtar matris seçimi;
Bir matrisin tersini almak için o matris bir kare matris olmalıdır.

2. Şifresiz matris boyutu seçimi : 
Şifresiz matrisin boyutunu 2x3 seçmemizin sebebi matris çarpımı yaparken birinci matrisin sütun sayısının ikinci matrisin satır sayısına eşit olmalıdır.

Bu sebeplerden dolayı ; 

Bu algoritmanın kodunu geliştirirken metinden gelen sayısal değerleri 2xn (n herhangi bir sayı olmak üzere) matrisi şekline zorladım ve anahtar matrisi de kullanıcının seçeneğine bırakmayarak her zaman 2x2 matrisi olarak aldım.

Metini matrise çevirirken algoritma yolu olarak :
1. Her karakter bir sayıya eşit olduğu için metindeki karakter sayısını buldum ve bu sayıyı bir değişkene eşitledim. Bu sayı uzunluk olsun.
2. Eğer uzunluk çift değilse metinin sonuna bir boşluk ekledim ki bunun da bir sayısal değeri var. Zaten metinin sonunda boşluk olması metinin içeriğini değiştirmeyeceği için bu konuda biraz rahat davrandım.
3. Eğer uzunluk çift ise metini ortadan ikiye böldüm ve sol tarafı matrisin ilk satırı , sağ tarafı da matrisin ikinci satırı olacak şekilde matrise dönüştürdüm.

ve sonrasında **Şifreleme İşlemi** başlığındaki şifreleme yöntemini uyguladım.

Kullanılan Modüller: 
Numpy
