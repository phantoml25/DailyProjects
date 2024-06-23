/*************************
 * Daily Project June 11th - Kevin Adams
 * 
 * Invert a Binary Tree
 * 
 ************************/

#include <random>
#include <iostream>
class BSTNode
{
public:
    int Key;
    BSTNode * Left;
    BSTNode * Right;
    BSTNode * Parent;
    
    void Insert(BSTNode * newNode)
    {
        switch ((*newNode).Key < Key)
        {
            case true: //Insert to left
                if (Left != nullptr)
                {
                    return Left->Insert(newNode);
                }
                else
                {
                    newNode->Parent = this;
                    Left = newNode;
                }
                
                break;
            case false: // Insert to right
                if (Right != nullptr)
                {
                    return Right->Insert(newNode);
                }
                else
                {
                    newNode->Parent = this;
                    Right = newNode;
                }
                
                break;
            default:
                break;
        } 
    };
    void Delete()
    {
        if (Left != nullptr)
        {
            Left->Delete();
        }
        if (Right != nullptr)
        {
            Right->Delete();
        }
        free(this);
    }
};

BSTNode * ReverseTree(BSTNode* Root)
{
    BSTNode * nRoot = new BSTNode;
    nRoot->Right = Root->Left;
    nRoot->Left = Root->Right;

    ReverseTree(nRoot->Left);
    ReverseTree(nRoot->Right);
    return nRoot;    
};

BSTNode * GenerateTree(int numNodes)
{
    BSTNode * Root = new BSTNode;
    Root->Key = 50;
    while (numNodes>0)
    {
        BSTNode * next = new BSTNode;
        next->Key = (rand() % 100);
        Root->Insert(next);
        numNodes--;
    }
}

void main()
{
    BSTNode * Root = GenerateTree(10);
    printf("Pause here to check tree");
    Root = ReverseTree(Root);
    printf("Pause here to check tree");
}