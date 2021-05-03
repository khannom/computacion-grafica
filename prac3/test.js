import * as THREE from '../../threejs/jsm/three.module.js';
import { GUI } from '../../threejs/jsm/dat.gui.module.js';
import {OrbitControls} from '../../threejs/jsm/OrbitControls.js';
import {OBJLoader} from '../../threejs/jsm/OBJLoader.js';
import {STLLoader} from '../../threejs/jsm/STLLoader.js';
import {MTLLoader} from '../../threejs/jsm/MTLLoader.js';


// utilizado cuando queremos poner la lampara dentro de la scene como un mesh
function makeXYZGUI(gui, vector3, name, onChangeFn) {
    const folder = gui.addFolder(name);
    folder.add(vector3, 'x', -20, 20).onChange(onChangeFn);
    folder.add(vector3, 'y', 0, 20).onChange(onChangeFn);
    folder.add(vector3, 'z', -20, 20).onChange(onChangeFn);
    folder.open();
}      

// utilizado por GUI para modificar los parametros de light en la scena
class ColorGUIHelper {
    constructor(object, prop) {
        this.object = object;
        this.prop = prop;
    }
    get value() {
        return `#${this.object[this.prop].getHexString()}`;
    }
    set value(hexString) {
        this.object[this.prop].set(hexString);
    }
}

// camera //////////////////////////////////////////////////
var aspect = window.innerWidth/window.innerHeight;
var camera = new THREE.PerspectiveCamera(75, aspect);
camera.position.set(0, 10, 20);

// scene //////////////////////////////////////////////////
var scene = new THREE.Scene();
scene.backgroundColor = new THREE.Color(0xffffff);
       
// mesh //////////////////////////////////////////////////    
////////////////////////////////////////////////////////////   
const cube_size = 4;      
var geometry_cube = new THREE.BoxGeometry(cube_size, cube_size, cube_size);
const texture_1 = new THREE.TextureLoader().load( '../../threejs/textures/texture_1.jpg' );
var material_1 = new THREE.MeshPhongMaterial( {map: texture_1 } );
var cube = new THREE.Mesh( geometry_cube, material_1 );
cube.position.set(0, cube_size / 2, 0);
cube.castShadow = true;
scene.add(cube); 

const geometry_plane = new THREE.PlaneGeometry( 50, 50, 32 );
const texture_2 = new THREE.TextureLoader().load( '../../threejs/textures/texture_2.jpg' );
const material_3 = new THREE.MeshPhongMaterial( {map: texture_2} );
const plane = new THREE.Mesh( geometry_plane, material_3 );
plane.rotation.x = Math.PI * -.5;
plane.receiveShadow = true;
scene.add( plane );
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////


// objloader////////////////////////////////////////////////    
//////////////////////////////////////////////////////////// 
/*var loader =  new OBJLoader();
loader.load(
    'models/poliedro.obj',
    function(object){
        object.position.set(5, -7, -10);                
        scene.add(object);
    }
)*/

// materioal loader and obj loader
var mtlLoader = new MTLLoader();
mtlLoader.load( '../../threejs/models/poliedro.mtl', function( materials ) {
    materials.preload();
    var objLoader = new OBJLoader();
    objLoader.setMaterials( materials );
    objLoader.load( '../../threejs/models/poliedro.obj', function ( object ) {
        object.position.set(5, -7, -10);   
        scene.add( object );
    });
});

// STLloader
var loader2 = new STLLoader();
    // Binary files - STL Import
loader2.load( '../../threejs/models/dragon.stl', function ( geometry ) {
    var material = new THREE.MeshLambertMaterial( { color: 0x00FF00 } );
    var mesh = new THREE.Mesh( geometry, material );
    
    mesh.scale.set( 0.1, 0.1, 0.1 );
    mesh.position.set( 0, cube_size, 0 );
    mesh.rotation.x = -Math.PI/2;
    scene.add( mesh );
} );
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
// HemisphereLight light ///////////////////////////////////
const skyColor = 0xB1E1FF;  // light blue
const groundColor = 0x59340B;  // black
const hemisphere_light = new THREE.HemisphereLight(skyColor, groundColor, 0.5);
scene.add(hemisphere_light);        
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
// DirectionalLight  ///////////////////////////////////////
const color = 0xFFFFFF;
const intensity = 0.5;
const light = new THREE.DirectionalLight(color, intensity);
light.position.set(5, 10, 10);
light.target.position.set(0, 0, 0);
scene.add(light);
scene.add(light.target);

const helper = new THREE.DirectionalLightHelper(light);
scene.add(helper);

function updateLight() {
    light.target.updateMatrixWorld();
    helper.update();
}
updateLight();        
// gui
const gui = new GUI();
gui.addColor(new ColorGUIHelper(light, 'color'), 'value').name('color');
gui.add(light, 'intensity', 0, 2, 0.01);
makeXYZGUI(gui, light.position, 'position', updateLight);
makeXYZGUI(gui, light.target.position, 'target', updateLight); 
//////////////////////////////////////////////////////////// 
////////////////////////////////////////////////////////////


// renderer //////////////////////////////////////////////////
var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );
renderer.render( scene, camera );

// OrbitControls /////////////////////////////////////////////
var controls = new OrbitControls( camera, renderer.domElement );

// axes ///////////////////////////////////////////////////////
const axesHelper = new THREE.AxesHelper( 15 );
scene.add( axesHelper );
        
// animation //////////////////////////////////////////////////
var animate = function(){
    requestAnimationFrame(animate);
    renderer.render( scene, camera );
}
animate();

// redimensioar  /////////////////////////////////////////////
window.addEventListener('resize', redimensionar);
function redimensionar(){
    camera.aspect = window.innerWidth/window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
    renderer.render( scene, camera );
}