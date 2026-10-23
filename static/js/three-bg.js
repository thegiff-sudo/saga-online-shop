/**
 * SAGA ONLINE SHOP - Interactive 3D WebGL Background Animation
 * Powered by Three.js
 * Features:
 * - Floating 3D golden logistics rings & faceted gem
 * - 150+ glowing 3D particles & connecting constellation nodes
 * - Smooth mouse parallax and gyro tilt response
 */

(function () {
  const canvas = document.getElementById("bg3dCanvas");
  if (!canvas || typeof THREE === "undefined") return;

  // Scene setup
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 28;

  const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    alpha: true,
    antialias: true,
    powerPreference: "high-performance",
  });
  renderer.setSize(canvas.parentElement.clientWidth, canvas.parentElement.clientHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Lights
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
  scene.add(ambientLight);

  const goldLight = new THREE.PointLight(0xf59e0b, 2.5, 60);
  goldLight.position.set(15, 12, 15);
  scene.add(goldLight);

  const blueLight = new THREE.PointLight(0x3b82f6, 2.0, 60);
  blueLight.position.set(-15, -10, 10);
  scene.add(blueLight);

  // Group for rotating elements
  const mainGroup = new THREE.Group();
  scene.add(mainGroup);

  // 1. Central 3D Golden Torus / Rings (representing Dropship Global Flow)
  const ringGeo1 = new THREE.TorusGeometry(8.5, 0.12, 16, 100);
  const ringMat1 = new THREE.MeshStandardMaterial({
    color: 0xf59e0b,
    metalness: 0.85,
    roughness: 0.25,
    wireframe: false,
    transparent: true,
    opacity: 0.65,
  });
  const ring1 = new THREE.Mesh(ringGeo1, ringMat1);
  ring1.rotation.x = Math.PI / 3;
  mainGroup.add(ring1);

  const ringGeo2 = new THREE.TorusGeometry(10.5, 0.08, 16, 100);
  const ringMat2 = new THREE.MeshStandardMaterial({
    color: 0x60a5fa,
    metalness: 0.9,
    roughness: 0.2,
    transparent: true,
    opacity: 0.45,
  });
  const ring2 = new THREE.Mesh(ringGeo2, ringMat2);
  ring2.rotation.y = Math.PI / 4;
  ring2.rotation.x = -Math.PI / 5;
  mainGroup.add(ring2);

  // 2. 3D Floating Golden Icosahedrons (Geometric Shopping nodes)
  const nodeGeo = new THREE.IcosahedronGeometry(1.6, 0);
  const nodeMat = new THREE.MeshStandardMaterial({
    color: 0xfbb03b,
    metalness: 0.8,
    roughness: 0.3,
    wireframe: true,
  });
  const nodeMesh = new THREE.Mesh(nodeGeo, nodeMat);
  nodeMesh.position.set(12, 4, -4);
  mainGroup.add(nodeMesh);

  const nodeMesh2 = nodeMesh.clone();
  nodeMesh2.scale.set(0.6, 0.6, 0.6);
  nodeMesh2.position.set(-14, -5, -6);
  mainGroup.add(nodeMesh2);

  // 3. 3D Glowing Particle Cloud (180 particles)
  const particleCount = 180;
  const particleGeo = new THREE.BufferGeometry();
  const positions = new Float32Array(particleCount * 3);
  const colors = new Float32Array(particleCount * 3);

  const goldColor = new THREE.Color(0xf59e0b);
  const blueColor = new THREE.Color(0x38bdf8);
  const whiteColor = new THREE.Color(0xffffff);

  for (let i = 0; i < particleCount; i++) {
    const i3 = i * 3;
    positions[i3] = (Math.random() - 0.5) * 60;
    positions[i3 + 1] = (Math.random() - 0.5) * 35;
    positions[i3 + 2] = (Math.random() - 0.5) * 30;

    // Mixed luxury colors
    const r = Math.random();
    const c = r < 0.55 ? goldColor : r < 0.85 ? blueColor : whiteColor;
    colors[i3] = c.r;
    colors[i3 + 1] = c.g;
    colors[i3 + 2] = c.b;
  }

  particleGeo.setAttribute("position", new THREE.BufferAttribute(positions, 3));
  particleGeo.setAttribute("color", new THREE.BufferAttribute(colors, 3));

  // Particle Material
  const particleMat = new THREE.PointsMaterial({
    size: 0.45,
    vertexColors: true,
    transparent: true,
    opacity: 0.85,
    blending: THREE.AdditiveBlending,
  });
  const particleSystem = new THREE.Points(particleGeo, particleMat);
  scene.add(particleSystem);

  // Mouse Parallax tracking
  let mouseX = 0;
  let mouseY = 0;
  let targetX = 0;
  let targetY = 0;

  window.addEventListener("mousemove", (e) => {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
    mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
  });

  // Touch parallax for mobile
  window.addEventListener(
    "touchmove",
    (e) => {
      if (e.touches.length > 0) {
        mouseX = (e.touches[0].clientX / window.innerWidth - 0.5) * 1.5;
        mouseY = (e.touches[0].clientY / window.innerHeight - 0.5) * 1.5;
      }
    },
    { passive: true }
  );

  // Resize handling
  window.addEventListener("resize", () => {
    if (!canvas || !canvas.parentElement) return;
    const width = canvas.parentElement.clientWidth;
    const height = canvas.parentElement.clientHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  });

  // Animation Loop
  let clock = new THREE.Clock();

  function animate() {
    requestAnimationFrame(animate);

    const delta = clock.getDelta();
    const time = clock.getElapsedTime();

    // Lerp mouse target for buttery smooth camera gliding
    targetX += (mouseX * 4 - targetX) * 0.05;
    targetY += (-mouseY * 3 - targetY) * 0.05;

    camera.position.x = targetX;
    camera.position.y = targetY;
    camera.lookAt(scene.position);

    // Rotate elements smoothly
    ring1.rotation.z += 0.004;
    ring1.rotation.y += 0.002;
    ring2.rotation.z -= 0.003;
    ring2.rotation.x += 0.003;

    nodeMesh.rotation.x += 0.008;
    nodeMesh.rotation.y += 0.01;
    nodeMesh.position.y = 4 + Math.sin(time * 1.5) * 0.8;

    nodeMesh2.rotation.x -= 0.01;
    nodeMesh2.rotation.z += 0.008;
    nodeMesh2.position.y = -5 + Math.cos(time * 1.2) * 0.6;

    // Slow drifting particle cloud
    particleSystem.rotation.y = time * 0.02;
    particleSystem.rotation.x = Math.sin(time * 0.01) * 0.05;

    renderer.render(scene, camera);
  }

  animate();
})();
