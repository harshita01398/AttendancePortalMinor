import React from 'react';
import Loading from './Loading';
class ButtonGroup extends React.Component{
    constructor(props){
        super(props);
        this.state = { file: '', loading: false ,file_name:''};
        this.uploadFile = this.uploadFile.bind(this);
        this.reader = new FileReader();
    }

    uploadFile(e){
        this.setState({file_name:e.target.files[0].name});
        this.reader.readAsDataURL(e.target.files[0]);
        console.log(e.target.files[0].name);
    }

    componentDidMount(){ // Life cycle method.
        this.reader.onload = () => {
            this.setState({ file: this.reader.result });
        };
        this.reader.onloadstart = () => {
            this.setState({ loading: true });
        };
        this.reader.onprogress = (data) => {
            this.setState({ loading: data.loaded/data.total*100 });
        };
        this.reader.onloadend = () => {
            this.setState({ loading: false })
        };
    }

    render(){
        return(
            <div>
            {
                this.state.loading ? <Loading progress={this.state.loading}/> :
                <div  className="choose">
                    <label  for ="img" className="label">Select an attendance sheet.</label>
                    <br></br><br></br>
                    <input type='file' accept={'image/* video/*'}  onChange={this.uploadFile} id = "img" style={{display:"none"}} />
                    <h4 style={{color : "lightblue"}}>{this.state.file_name}</h4>
                    <img src={this.state.file} alt = "No sheet chosen"  style = {{width : '700px',height: '400px'}} />
                    <br></br>
                    <br></br>
                    <button className="convert"> Convert </button>
                </div>
            }
            </div>
    );
    }
}

export default ButtonGroup;