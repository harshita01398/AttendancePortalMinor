import React from 'react';
import Loading from './Loading';
import styles from './Layout.css';

class ButtonGroup extends React.Component{
    constructor(props){
        super(props);
        this.state = { file: '', loading: false ,file_name:''};
        this.reader = new FileReader();
        this.uploadFile = this.uploadFile.bind(this);
        this.convertFile = this.convertFile.bind(this);
    }

    uploadFile(e){
        this.setState({file_name:e.target.files[0].name});
        this.reader.readAsDataURL(e.target.files[0]);
        // console.log(e.target.files[0].name);
    }

    convertFile(e){
        console.log(e.target);
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
                <div>
                    <img src="background.jpg" style={{ position: 'absolute', height: 'auto', width: 'auto' }} />
                    <div style={{ position: 'absolute' , top: '50px' , left:'40%' , color: 'azure' , fontSize: '80px' }}>eXtractor</div>
                </div>
            {
                this.state.loading ? <Loading progress={this.state.loading}/> :
                <div  className="choose">
                    <label className="label" htmlFor={"img"}>Select an attendance sheet.</label>
                    <input type='file' accept={'image/*'}  onChange={this.uploadFile} id = "img" style={{display:"none"}} />
                    <h4 style={{color : "lightblue"}}>{this.state.file_name}</h4>
                    <img src={this.state.file} alt = "No sheet chosen"  style = {{width : '700px',height: '400px'}} />
                    <div>
                        <button className="convert" disabled={!this.state.file} onClick={this.convertFile}> Convert </button>
                    </div>
                </div>
            }
            </div>
    );
    }
}

export default ButtonGroup;