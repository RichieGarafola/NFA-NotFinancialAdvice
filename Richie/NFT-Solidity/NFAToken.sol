// SPDX-License-Identifier: Richie Garafola Mark Staten Jacob Edelbrock

/*
NFA-Token 
*/

// Add the pragma statement
pragma solidity ^0.8.4;

// Import the `ERC1155` 'ERC1155Burnable',  `ERC1155Supply`, 'Ownable', and 'Pausable' contracts from OpenZeppelin. These contracts implement the `ERC1155` standards that we’ll use to build our contract. Import these contracts by using the following code:

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC1155/ERC1155.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/security/Pausable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC1155/extensions/ERC1155Burnable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC1155/extensions/ERC1155Supply.sol";


// Define a contract named `NFAToken` that inherits the OpenZeppelin `ERC1155` 'ERC1155Burnable',  `ERC1155Supply`, 'Ownable', and 'Pausable' contracts.
contract NFAToken is ERC1155, Ownable, Pausable, ERC1155Burnable, ERC1155Supply
 {
    // Use the following code to create a constructor that will configure the `NFAToken` contract and the `ERC1155` 'ERC1155Burnable',  `ERC1155Supply`, 'Ownable', and 'Pausable' contract:
        uint256 public constant GOLD = 0;
        uint256 public constant SILVER = 1;
        uint256 public constant BRONZE = 2;
    constructor() ERC1155("") {
        _mint(msg.sender, GOLD, 20, "");
        _mint(msg.sender, SILVER, 50, "");
        _mint(msg.sender, BRONZE, 100, "");
    }
    function setURI(
        string memory newuri
        ) 
        public onlyOwner {
        _setURI(newuri);
    }

    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }


    function mintBatch(
        address to, 
        uint256[] memory ids, 
        uint256[] memory amounts, 
        bytes memory data
        )
        public
        onlyOwner
    {
        _mintBatch(to, ids, amounts, data);
    }
    function mint(
        address account,
        uint256 id, 
        uint256 amount, 
        bytes memory data
        )
        public
       // onlyOwner
    {
        _mint(account, id, amount, data);
    }

    function _beforeTokenTransfer(
        address operator, 
        address from, 
        address to, 
        uint256[] memory ids, 
        uint256[] memory amounts, 
        bytes memory data
        )
        internal
        whenNotPaused
        override(ERC1155, ERC1155Supply)
    {
        super._beforeTokenTransfer(
            operator, 
            from, 
            to, 
            ids, 
            amounts, 
            data
            );
        require(
            from == address(0) || to == address(0), 
            "Not allowed to transfer token"
            );
    }
}