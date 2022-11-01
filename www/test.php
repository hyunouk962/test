<?php
//$a= $b= $c= 1100;
//print ($a.$b.$c);
#python def php,javascript function 
#python는 dictionary, 자바 는 map,웹에서는 json ,php 연관배열(associative array, hash, dictionary)
# php $asd = (''=>'');
# python
/*
dic1 = {
    'Name':'kim',
    'City' : 'Seoul'
    }
dic2 = dict([
    ('Name','kim'),
    ('City' , 'Seoul')
])
dic3 = dict(
    Name ='kim',
    City = 'Seoul'
)
*/

#연산자
# php 
/*
if() print('false')
elseif() print('??')
else print('good')

print(5+3 == 8 and !8>7);
*/
# python
/*
sss=2
if sss == 1:
    print('false')
elif sss == 2:
    print('??')
else:
    print('good')
    
print(5+3 == 8 and not 8>7);
    */
    /*
    python Class
    class Dogs:#object 상속 Dog: ,Dog():, Dog(object)
    #클래스 속성
    species = 'firstdog'
    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info (self):
        return '{} is {} years old'.format(self.name,self.age)
    def speak(self,sound):
        return '{} says {}!'.format(self.name, sound)
    php class
    $this 현재 객체(),self::는 현제 클래스 참조
    //$a = new A();
    //$a->foo();
    //A::foo();
    
    class Dogs{
        public $species = 'firstdog';
        public function init($name,$age){
            $this->name = $name;
            $this->age = $age;
        }
        public function info(){
           return ''.$this->name.' is '.$this->age.' year old';
        }
        public function speak($sound){
           return ''.$this->name.' say '.$sound.'!!';
        }
    }
    $dogclass = new Dogs();
    $dogclass->init('test',3);
    print($dogclass->info());
    print($dogclass->speak('wal wal'));
    */
    
?>