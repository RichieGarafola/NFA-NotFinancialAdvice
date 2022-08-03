// SPDX-License-Identifier: Richie Garafola Mark Staten Jacob Edelbrock

/*
NFA-Token 
*/

// Add the pragma statement
pragma solidity ^0.8.4;

// Import the `ERC1155` 'ERC1155Burnable',  `ERC1155Supply`, 'Ownable', and 'Pausable' contracts from OpenZeppelin. These contracts implement the `ERC1155` standards that we’ll use to build our contract. Import these contracts by using the following code:

import "@openzeppelin/contracts@4.7.2/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts@4.7.2/access/Ownable.sol";
import "@openzeppelin/contracts@4.7.2/security/Pausable.sol";
import "@openzeppelin/contracts@4.7.2/token/ERC1155/extensions/ERC1155Burnable.sol";
import "@openzeppelin/contracts@4.7.2/token/ERC1155/extensions/ERC1155Supply.sol";

// Define a contract named `NFAToken` that inherits the OpenZeppelin `ERC1155` 'ERC1155Burnable',  `ERC1155Supply`, 'Ownable', and 'Pausable' contracts.
contract NFAToken is ERC1155, Ownable, Pausable, ERC1155Burnable, ERC1155Supply {
// Define a contract named `NFAToken` that inherits the OpenZeppelin `ERC1155` 'ERC1155Burnable',  `ERC1155Supply`, 'Ownable', and 'Pausable' contracts.    
    constructor() ERC1155("") {}
    // Use the following code to create a constructor that will configure the `NFAToken` contract and the `ERC1155` 'ERC1155Burnable',  `ERC1155Supply`, 'Ownable', and 'Pausable' contract:

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

    function mint(
        address account,
        uint256 id, 
        uint256 amount, 
        bytes memory data
        )
        public
        onlyOwner
    {
        _mint(account, id, amount, data);
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