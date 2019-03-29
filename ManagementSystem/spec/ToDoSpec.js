describe('Testing the functionality, this is the checklist', ()=>{
      it('should add an item', ()=>{
        let todo = new ToDo();
        let item = {
         title: "get milk",
         complete: false
       }
        const done = todo.addTodo(item)
        expect(todo.getItems().length).toBe(1);
      })
    })

describe('Testing addition', ()=>{
      it('should add an item', ()=>{
        let x=2;
        let y=8;
        let z= addition(x,y);
        expect(z).toBe(10);
      })
    })