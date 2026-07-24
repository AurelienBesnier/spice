# Use an official ROCm development image as the base
FROM rocm/dev-ubuntu-24.04:7.2

# Set environment variables for ROCm and HIPRT
ENV HIP_PATH=/opt/rocm
ENV DEBIAN_FRONTEND=noninteractive

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    cmake \
    build-essential \
    python3 \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Git LFS (required to fetch HIPRT test resources, optional but recommended)
RUN apt-get update && apt-get install -y git-lfs && git lfs install

# Clone the HIPRT repository
WORKDIR /opt
RUN git clone https://github.com/GPUOpen-LibrariesAndSDKs/HIPRT.git --recursive

# Build HIPRT
WORKDIR /opt/HIPRT
RUN mkdir build && cd build && \
    cmake -DCMAKE_BUILD_TYPE=Release \
          -DBITCODE=OFF \
          -DHIP_PATH=${HIP_PATH} \
          .. && \
    cmake --build . --config Release -j$(nproc)

# (Optional) Set up working directory for your application
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -a && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

# Set up application directory
WORKDIR /code
COPY . .


ENTRYPOINT ["/bin/bash", "-l"]