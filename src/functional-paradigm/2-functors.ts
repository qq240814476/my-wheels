// store value 
// has map function, map return a new functor to finish the chain
// Maybe 
// Either
// pointer, both Maybe and Either belong pointer, because they have of function

declare type FNType = (a: number) => any;
function Maybe(val: number) {
  this.val = val;
  this.of = function(val: number) {
    return new Maybe(val);
  }
  this.map = function(f: FNType) {
    return this.of((this.val === null || this.val===undefined) ? null : f(this.val));
  }
}

const maybe = new Maybe(4).map((a) => a+1).map((a) => null).map((a) => a*a);
// maybe{ val: null }
// which map is wrong

function Some (val: number){
  this.val =val;
  this.of = function (val: number){
    return new Some(val);
  }
  this.map = function (f: FNType){
    return this.of(f(this.val));
  }
}
function Nothing(val: number){
  this.val = val;
  this.of = function(val: number){
    return new Nothing(val);
  }
  this.map = function(f: FNType){
    return this.of(this.val);
  }
}

const Either = {
  Some,
  Nothing,
}

function getMessage(val: number){
  let res;
  try{
    res = doSomething(val);
  } catch (e){
    return Either.Nothing(401);
  }
  return Either.Some(res);
}

const either = new Either.Some(2).map(getMessage).map(a => a + a);
// Nothing{ val: 401 }

// 单态 和 双态 的区别, help us to record error info