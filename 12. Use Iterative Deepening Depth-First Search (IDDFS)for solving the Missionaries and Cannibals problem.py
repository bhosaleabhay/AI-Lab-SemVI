class State:
    def __init__(self,cannibalL,missionaryL,boatPosition,cannibalR,missionaryR):
        self.cannibalL=int(cannibalL)
        self.missionaryL=int(missionaryL)
        self.cannibalR=int(cannibalR)
        self.missionaryR=int(missionaryR)
        self.boatPosition=boatPosition
        self.parentState=None
        
    def isValid(self,state):
        if state.missionaryL >= 0 and state.missionaryR >= 0 and state.cannibalL >= 0 and state.cannibalR >= 0 and (state.missionaryL == 0 or state.missionaryL >= state.cannibalL) and (state.missionaryR == 0 or state.missionaryR >= state.cannibalR): 
            return True
        return False
    		
    def testAndAdd(self,successors,newState):
	    if self.isValid(newState):
	        newState.parentState=self
	        successors.append(newState)
	    return
		
    def generateSuccessors(self):
        successors=[]
        if(self.boatPosition=="LEFT"):
            self.testAndAdd(successors,State(self.cannibalL,self.missionaryL - 2,"RIGHT",self.cannibalR,self.missionaryR + 2)) # Two missionaries cross left to right.
            self.testAndAdd(successors,State(self.cannibalL - 2, self.missionaryL, "RIGHT",self.cannibalR + 2, self.missionaryR)) # Two cannibals cross left to right.
            self.testAndAdd(successors, State(self.cannibalL - 1, self.missionaryL - 1, "RIGHT",self.cannibalR + 1, self.missionaryR + 1)) # One missionary and one cannibal cross left to right.
            self.testAndAdd(successors, State(self.cannibalL, self.missionaryL - 1, "RIGHT",self.cannibalR, self.missionaryR + 1)) # One missionary crosses left to right.
            self.testAndAdd(successors, State(self.cannibalL - 1, self.missionaryL, "RIGHT",self.cannibalR + 1, self.missionaryR)) # One cannibal crosses left to right
        else:
            self.testAndAdd(successors, State(self.cannibalL, self.missionaryL + 2,"LEFT",self.cannibalR, self.missionaryR - 2)) # Two missionaries cross right to left.
            self.testAndAdd(successors, State(self.cannibalL + 2, self.missionaryL,"LEFT",self.cannibalR - 2, self.missionaryR)) # Two cannibals cross right to left.
            self.testAndAdd(successors, State(self.cannibalL + 1, self.missionaryL + 1,"LEFT",self.cannibalR - 1, self.missionaryR - 1)) # One missionary and one cannibal cross right to left.
            self.testAndAdd(successors, State(self.cannibalL, self.missionaryL + 1,"LEFT",self.cannibalR, self.missionaryR - 1)) # One missionary crosses right to left.
            self.testAndAdd(successors, State(self.cannibalL + 1, self.missionaryL,"LEFT",self.cannibalR - 1, self.missionaryR)) # One cannibal crosses right to left
        return successors
		

def recursive_dls(state,limit):
    if state.cannibalL==0 and state.missionaryL==0:
        return state
    elif limit==0:
        return None
    else:
        successors=state.generateSuccessors()
        for child in successors:
            result=recursive_dls(child,limit-1)
            if(result!=None):
                return result
        return None

def dls(initial_state):
    limit=20
    return recursive_dls(initial_state,limit)
    
			
state=State(3,3,"LEFT",0,0)
state.parentState=None
solution=dls(state)
if solution==None:
    print("No solution was found")
else:
    path=[]
    child=solution
    while(child!=None):
        path.append(child)
        child=child.parentState
    depth=len(path)-1
    print("C-L  M-L  Boat  C-R  M-R")
    for i in range(depth,-1,-1):
        child=path[i]
        print(f"({child.cannibalL}    {child.missionaryL}   {child.boatPosition}   {child.cannibalR}   {child.missionaryR})")
        print()
    
        