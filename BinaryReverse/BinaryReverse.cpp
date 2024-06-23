/*************************
 * Daily Project June 11th - Kevin Adams
 *
 * Invert a Binary Tree
 *
 ************************/

#include <iostream>
#include <random>
#include <iostream>
class BSTNode
{
public:
    int Key;
    BSTNode* Left = nullptr;
    BSTNode* Right = nullptr;
    BSTNode* Parent = nullptr;

    void Insert(BSTNode* newNode)
    {
        switch (newNode->Key < this->Key)
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

BSTNode* ReverseTree(BSTNode* Root)
{
    bool left = false;
    bool right = false;
    BSTNode* nRoot = new BSTNode;
    if (Root->Parent == nullptr) {
        nRoot->Key = Root->Key;
    }
    if (Root->Left != nullptr){
        nRoot->Right = Root->Left;
        right = true;
    }
    if (Root->Right != nullptr) {
        nRoot->Left = Root->Right;
        left = true;
    }

    if (left){
        ReverseTree(nRoot->Left);
    }
    if (right) {
        ReverseTree(nRoot->Right);
    }

    return nRoot;
};

BSTNode* GenerateTree(int numNodes)
{
    BSTNode* Root = new BSTNode;
    Root->Key = 50;
    while (numNodes > 0)
    {
        BSTNode* next = new BSTNode;
        next->Key = (rand() % 100);
        Root->Insert(next);
        numNodes--;
    }
    return Root;
}

void printBT(const std::string& prefix, const BSTNode* node, bool isLeft)
{
    if (node != nullptr)
    {
        std::cout << prefix;

        std::cout << (isLeft ? "├──" : "└──");

        // print the value of the node
        std::cout << node->Key << std::endl;

        // enter the next tree level - left and right branch
        printBT(prefix + (isLeft ? "│   " : "    "), node->Left, true);
        printBT(prefix + (isLeft ? "│   " : "    "), node->Right, false);
    }
}

void printBT(const BSTNode* node)
{
    printBT("", node, false);
}

void main()
{
    BSTNode* Root = GenerateTree(10);
    printBT(Root);
    Root = ReverseTree(Root);
    printBT(Root);
}
