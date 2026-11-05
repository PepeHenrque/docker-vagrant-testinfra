# Vagrantfile – fase 2 (root)
Vagrant.configure('2') do |config|
  # ---- VM base -------------------------------------------------
  config.vm.box = 'ubuntu/focal64'
  config.vm.hostname = 'testinfra-vm'

  # ---- Rede ----------------------------------------------------
  config.vm.network 'forwarded_port', guest: 80, host: 8080
  config.vm.network 'forwarded_port', guest: 22, host: 2222, host_ip: "0.0.0.0"

  # ---- Pastas compartilhadas ------------------------------------
  config.vm.synced_folder './', '/vagrant'

  # ---- Docker (placeholder) ------------------------------------
  # A imagem real será definida na fase 1 (Dockerfile).
  # Quando a branch feat/dockerfile for mergeada, substitua
  #   <docker-image-name>  por  nome da imagem publicada.
  config.vm.provision 'docker' do |d|
    d.run 'app',
      image: '<docker-image-name>',   # TODO: atualizar após fase 1
      args: '-p 8080:80'
  end

  # ---- Provisionamento adicional (shell) -----------------------
  config.vm.provision 'shell', path: 'bootstrap.sh'
end
