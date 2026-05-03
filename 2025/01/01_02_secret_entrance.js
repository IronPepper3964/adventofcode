// https://adventofcode.com/2025/day/1
//
// Rules:
// Dial starts at 50
// `L` lines decrease the number
// `R` lines increase the number
// 0 is the minimum number, 99 is the max, numbers roll over
const fs = require('fs');
const { type } = require('os');

const run_example = false; // Set if using the example puzzle text or full text

const puzzle_file = './input/aoc01_01.txt';
const example_puzzle_file = './input/aoc01_example.txt';
const puzzle_eol = '\n';
const example_puzzle_eol = '\r\n'; // Copy/pase of example puzzle text keeps the windows EOL characters.


// Read puzzle input
function readPuzzleFile(inFileName, eol = '\n') {
  try {
    return fs.readFileSync(inFileName, 'utf8').split(eol);
  } catch (err) {
    console.error('Error reading file:', err);
  }
}
const puzzle_array = readPuzzleFile(run_example ? example_puzzle_file : puzzle_file, run_example ? example_puzzle_eol : puzzle_eol);

// Helper functions
function parse_rotation(rotation){
  return {
    dir: rotation.charAt(0),
    fullRotationCount: parseInt(rotation.substring(1)/100),
    rotationRemainder: rotation.substring(1)%100
  };
}

function rollover_adjust(position)
{
  if (position >= 0 && position <= 99)
    return position

  if (position < 0)
    position = 100 + position
  else if (position > 99)
    position = position - 100

  return position
}

let current_position = 50;
let zero_count = 0;
let previous_position = current_position

let r = puzzle_array.length;

for (let i = 0; i < r; i++){
  previous_position = current_position
  console.log("Starting Position: " + current_position);
  console.log(puzzle_array[i]);
  curr_rotation = parse_rotation(puzzle_array[i]);
  console.log(typeof curr_rotation);
  console.log(curr_rotation.dir);

  //Add full rotations
  zero_count += curr_rotation.fullRotationCount
  
  if (curr_rotation.dir == "L")
  {
    console.log("Left!")
    curr_rotation.rotationRemainder = -curr_rotation.rotationRemainder
  }
  console.log("Rot: " + curr_rotation.rotationRemainder);

  current_position = current_position + curr_rotation.rotationRemainder;

  // determine if 0 was passed
  if ((current_position > 99 || current_position <= 0) && previous_position != 0)
    zero_count += 1

  current_position = rollover_adjust(current_position);

  console.log(current_position);

  console.log("current zero count: " + zero_count)
}

console.log("Solution:" + zero_count);