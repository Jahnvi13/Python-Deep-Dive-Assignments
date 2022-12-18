// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

//the smart contract class which extends ERC721, ERC721URIStorage, Ownable
contract MyContract is ERC721, ERC721URIStorage, Ownable
{
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    constructor() ERC721("MyToken", "MTK") {}
    // function to mint the NFTs,only owner can mint as nothing was specified
    // takes in the adress and the uri of the image metadata
    function safeMint(address to, string memory uri) public onlyOwner 
    {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment(); //everytime NFT is minted, the tokenid is incremented
        _safeMint(to, tokenId); //calls the ERC721 standard minting function
        _setTokenURI(tokenId, uri);//calls the ERC721 standard setTokenURI 
    }
    // the burn and tokenURI functions need to be overridden to use ERC721 and ERC721URIStorage to store metadata
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) 
    {
        super._burn(tokenId);
    }
    function tokenURI(uint256 tokenId) public view override(ERC721, ERC721URIStorage)
    returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

}
