function _add(a, b, c, d){
  return a + b + c + d;
}
declare type FNCurry = (...args: Array<any>) => any;
function curry(func: FNCurry){
  const g = (...args: Array<any>) => {
    if(args.length >= func.length){
      return func(...args);
    } else {
      return (...left: Array<any>) => {
        return g(...args, ...left);
      }
    }
  }
  return g;
}

const add = curry(_add);
console.log(add(1, 2)(3)(4));
console.log(add(1)(2)(3)(4));
console.log(add(1,2,3)(4));
console.log(add(1,2)(3,4));
