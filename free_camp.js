// @ts-check
/* eslint-disable no-console */

const printNumbers = (initialNumber) => {
    // BEGIN (write your solution here)
    while (initialNumber >= 1) {
      console.log(initialNumber);
      initialNumber -= 1;
    }
    return initialNumber + 'finished!';
    // END
  };
  
  export default printNumbers;
  