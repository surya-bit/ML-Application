import React, { useState } from 'react';

const DropdownMenu = ({selectedOption, setSelectedOption}) => {
  // State to track whether the dropdown is open or closed
  const [isOpen, setIsOpen] = useState(false);

  // State to track the selected option
  

  // Array of options for the dropdown
  const options = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

  // Function to handle when an option is selected
  const handleOptionSelect = (option) => {
    setSelectedOption(option);
    setIsOpen(false); // Close the dropdown after selection
  };

  return (
    <div className="">
      {/* Button to toggle the dropdown */}
      <button onClick={() => setIsOpen(!isOpen)}>
      <div className=' bg-sky-500 rounded-full font-black p-2 w-80 '>
        {selectedOption ? selectedOption : 'Click here to choose a month'}
        </div>
        </button>

      {/* Dropdown menu */}
      {isOpen && (
        <ul className='bg-white border-2 h-auto rounded-xl mt-5' >
          {options.map((option) => (
            
            
            <li 
            className='p-5 mx-5  border-y'
            key={option} onClick={() => handleOptionSelect(option)}>
              {option}
            </li>
            
            
          ))}
        </ul>
      )}
    </div>
  );
};

export default DropdownMenu;
